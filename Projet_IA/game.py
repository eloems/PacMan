from ghost import Ghost
from pacman import Pacman
from pathlib import Path

import utils,pygame

class Game:
    def __init__(self, lvl = 1):
        self.level = lvl
        self.grid = utils.LEVEL[self.level]
        self.pacman_alive=True
        
        pos_p = self.init_pos(utils.PACMAN_CHAR,1)
        self.pacman = Pacman(pos_p)
        
        pos_g = self.init_pos(utils.GHOST_CHAR,2)
        self.ghosts = Ghost(pos_g)
        
        self.score = 0
        self.nbr_items = self.init_nbr_items()

    # Get the position of the element ( nbr is the number of this element to find)
    def init_pos(self,target_char,nbr):
        i=0
        pos =[]
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == target_char :
                    pos.append((row,col))
                    i+=1
                    if i==nbr and nbr==1 :
                        return (row,col)
                    elif i==nbr :
                        return pos
                    
    def init_nbr_items(self):
        nbr=0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == utils.ITEM_CHAR :
                    nbr+=1
        return nbr
        
    def is_pacman_alive(self):
        return self.pacman_alive

    def game_over(self):
        self.pacman_alive = False
        
    def is_win(self):
        return self.score == self.nbr_items
    
    def print_grid(self):
        for row in range(len(self.grid)):
            print(''.join(self.grid[row]))
            
    def next_level(self) :
        self.level = self.level +1
        self.grid = utils.LEVEL[self.level]
        
        self.pacman_alive=True
        
        pos_p = self.init_pos(utils.PACMAN_CHAR,1)
        self.pacman = Pacman(pos_p)
        
        pos_g = self.init_pos(utils.GHOST_CHAR,2)
        self.ghosts = Ghost(pos_g)
        
        self.score = 0
        self.nbr_items = self.init_nbr_items()
        

    def start(self):
        while self.is_pacman_alive() and not self.is_win():
            self.next_state()
            self.print_grid()           
        return self.is_win()
    
    def get_grid_base(self, width, height):
        menu_start = width * 2 / 3
        vertical_gap = (height - 1) // len(self.grid)
        horizontal_gap = (menu_start - 1) // len(self.grid[0])
        gap = min(horizontal_gap, vertical_gap)
        vertical_start = (height - len(self.grid) * gap) // 2
        horizontal_start = (menu_start - len(self.grid[0]) * gap) // 2
        return gap, vertical_start, horizontal_start, menu_start


    def next_state(self,move = None):
        mv_pacman = None
        if move != None :
            mv_pacman = self.pacman.setMovePacman(move,self.grid)
        else :
            mv_pacman = self.pacman.getMovePacman(self.grid)
        mv_ghost = self.ghosts.getMoveGhost(self.grid, self.pacman.direction)
        self.apply_mv(mv_ghost,mv_pacman)


    def apply_mv(self,g,p):

        pacman_oldpos = p[0]
        pacman_newpos = p[1]
        for i in range(len(g)):
            ghost_oldpos = g[i][0]
            ghost_newpos = g[i][1]

            if ghost_newpos == pacman_newpos or ( ghost_newpos == pacman_oldpos and pacman_newpos == ghost_oldpos ) :
                self.grid[ghost_oldpos[0]][ghost_oldpos[1]] = utils.EMPTY_CHAR
                self.grid[pacman_oldpos[0]][pacman_oldpos[1]] = utils.EMPTY_CHAR
                self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_CHAR
                self.game_over()
                return False
            if self.grid[ghost_oldpos[0]][ghost_oldpos[1]]== utils.GHOST_GHOST_CHAR :
                self.grid[ghost_oldpos[0]][ghost_oldpos[1]] = utils.GHOST_CHAR
            elif self.grid[ghost_oldpos[0]][ghost_oldpos[1]]== utils.GHOST_ITEM_CHAR :
                self.grid[ghost_oldpos[0]][ghost_oldpos[1]] = utils.ITEM_CHAR
            else :
                self.grid[ghost_oldpos[0]][ghost_oldpos[1]] = utils.EMPTY_CHAR
                
            if self.grid[pacman_oldpos[0]][pacman_oldpos[1]]!= utils.GHOST_CHAR :
                self.grid[pacman_oldpos[0]][pacman_oldpos[1]] = utils.EMPTY_CHAR
                
            if self.grid[ghost_newpos[0]][ghost_newpos[1]]== utils.ITEM_CHAR :
                self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_ITEM_CHAR
            elif self.grid[ghost_newpos[0]][ghost_newpos[1]]== utils.GHOST_CHAR :
                self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_GHOST_CHAR
            elif self.grid[ghost_newpos[0]][ghost_newpos[1]]== utils.EMPTY_CHAR :
                self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_CHAR
                   
            if self.grid[pacman_newpos[0]][pacman_newpos[1]]== utils.ITEM_CHAR :
                self.grid[pacman_newpos[0]][pacman_newpos[1]] = utils.PACMAN_CHAR
                self.score+=1
            elif self.grid[pacman_newpos[0]][pacman_newpos[1]]== utils.EMPTY_CHAR:
                self.grid[pacman_newpos[0]][pacman_newpos[1]] = utils.PACMAN_CHAR

class GUIGame(Game):
    DEFAULT_WIDTH = 900
    DEFAULT_HEIGHT =600
    DEFAULT_TITLE_FONT_SIZE = 40
    DEFAULT_FONT_SIZE = 20

    def __init__(self):
        super(GUIGame,self).__init__()

    def next_tick(self,agent ):
        while self.is_pacman_alive() and not self.is_win():
            self.process_event(agent)
            if agent != None :
                self.next_state()
            pygame.time.wait(150)
            self.draw()
            
    def end_level(self, agent):
        self.draw(True)
        pygame.time.wait(1500)
        if self.is_win() :
            if self.level + 1 <= 2 : 
                self.next_level()
                self.next_tick(agent)
        
    def init_pygame(self):
        pygame.init()
        pygame.font.init()
        self.set_window_size(GUIGame.DEFAULT_WIDTH, GUIGame.DEFAULT_HEIGHT)
        pygame.display.set_caption(utils.TITLE)
        
    def process_event(self, agent):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                self.cleanup_pygame()
                
            elif event.type == pygame.KEYDOWN and agent == None:
                if event.key == pygame.K_UP:
                    self.next_state(utils.UP)
                elif event.key == pygame.K_RIGHT:
                    self.next_state(utils.RIGHT)
                elif event.key == pygame.K_DOWN:
                    self.next_state(utils.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.next_state(utils.LEFT)

            elif event.type == pygame.VIDEORESIZE:
                self.set_window_size(event.w, event.h)


    def set_window_size(self,width,height):
        self.screen = pygame.display.set_mode(size=(width,height), flags = pygame.RESIZABLE)
        ratio = min(width / GUIGame.DEFAULT_WIDTH, height / GUIGame.DEFAULT_HEIGHT,)
        self.title_font = pygame.font.Font(
            Path("Fonts") / Path("CrackMan.ttf"),
            round(GUIGame.DEFAULT_TITLE_FONT_SIZE * ratio),
        )
        self.normal_font = pygame.font.Font(
            Path("Fonts") / Path("namco.ttf"),
            round(GUIGame.DEFAULT_FONT_SIZE * ratio),
        )

    def get_coord(self, screen, pos):
        gap, vertical_start, horizontal_start, menu_start = self.get_grid_base(screen.get_width(), screen.get_height())
        x,y = pos
        i = int((y - vertical_start) // gap)
        j = int((x - horizontal_start) // gap)
        return i,j
    
    def draw_cells(self, screen, gap, vertical_start, horizontal_start):
        
        img_item = pygame.image.load(utils.ITEM_IMG)
        img_item.convert()
        img_item = pygame.transform.scale(img_item,(gap,gap))

        img_wall = pygame.image.load(utils.WALL_IMG)
        img_wall.convert()
        img_wall = pygame.transform.scale(img_wall,(gap,gap))

        img_ghost1 = pygame.image.load(utils.GHOST1_IMG)
        img_ghost1.convert()
        img_ghost1 = pygame.transform.scale(img_ghost1,(gap,gap))
        
        img_ghost2 = pygame.image.load(utils.GHOST2_IMG)
        img_ghost2.convert()
        img_ghost2 = pygame.transform.scale(img_ghost2,(gap,gap))
        
        img_ghost1_2 = pygame.image.load(utils.GHOST1_2_IMG)
        img_ghost1_2.convert()
        img_ghost1_2 = pygame.transform.scale(img_ghost1_2,(gap,gap))
        
        img_pacman = pygame.image.load(utils.PACMAN_IMG)
        if self.pacman.direction == utils.DOWN :
            img_pacman = pygame.image.load(utils.PACMAN_DOWN_IMG)
        elif self.pacman.direction == utils.UP :
            img_pacman = pygame.image.load(utils.PACMAN_UP_IMG)
        elif self.pacman.direction == utils.LEFT :
            img_pacman = pygame.image.load(utils.PACMAN_LEFT_IMG)
        elif self.pacman.direction == utils.RIGHT :
            img_pacman = pygame.image.load(utils.PACMAN_RIGHT_IMG)
        img_pacman.convert()
        img_pacman = pygame.transform.scale(img_pacman,(gap,gap))
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != utils.EMPTY_CHAR:
                    if self.grid[i][j] == utils.WALL_CHAR:
                        img_cell = img_wall
                    elif self.grid[i][j] == utils.PACMAN_CHAR:
                        img_cell = img_pacman
                    elif self.grid[i][j] == utils.ITEM_CHAR:
                        img_cell = img_item
                    elif self.grid[i][j] == utils.GHOST_CHAR or self.grid[i][j] == utils.GHOST_ITEM_CHAR :
                        if self.ghosts.ghosts[1] == (i,j):
                            img_cell = img_ghost1
                        else :
                            img_cell = img_ghost2
                    elif self.grid[i][j] == utils.GHOST_GHOST_CHAR :
                        img_cell = img_ghost1_2
                        
                    screen.blit(img_cell,(horizontal_start + j * gap,vertical_start + i * gap))

    def draw(self,end = False):
        self.screen.fill(utils.BLACK)
        width, height = self.screen.get_size()

        gap, vertical_start, horizontal_start, menu_start = self.get_grid_base(
            width, height
        )

        self.draw_cells(self.screen, gap, vertical_start, horizontal_start)
        pygame.draw.line(
            self.screen, utils.GREY, (menu_start, 0), (menu_start, height)
        )

        title = self.title_font.render(utils.TITLE, True, utils.WHITE)
        score = self.normal_font.render(
            "score: " + str(self.score), True, utils.WHITE
        )

        self.screen.blit(
            title,
            (
                menu_start + (width - menu_start) / 2 - title.get_width() / 2,
                height * (1 / 15) - title.get_height() / 2,
            ),
        )
        self.screen.blit(
            score,
            (
                menu_start + (width - menu_start) / 7,
                height * (3 / 15) - score.get_height() / 2,
            ),
        )

        if end :
            text_end = None
            if self.is_win():
                text_end = self.normal_font.render( " you win ! ",True, utils.RED)
            else :
                text_end = self.normal_font.render( " game over ", True, utils.RED)
            self.screen.blit(
                text_end,
                (
                menu_start + (width - menu_start) / 2 - title.get_width() / 2,
                    height * (1 / 2) - score.get_height() / 2,
                ),
            )

        pygame.display.flip()

    def cleanup_pygame(self):
        pygame.font.quit()
        pygame.quit()
        
        
        
        
    

        
                
            
        
        

    
            
