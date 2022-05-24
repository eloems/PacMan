from ghost import Ghost

import utils

class Game:
    def __init__(self):
        self.run = True
        self.grid = utils.LEVEL_1
        self.pacman_alive=True
        self.pacman_pos = self.init_pos(utils.PACMAN_CHAR,1)
        pos_g = self.init_pos(utils.GHOST_CHAR,2)
        self.ghosts = Ghost(pos_g)
        self.pacman_direction = None
        self.score = 0
        self.nbr_items = self.init_nbr_items()
        
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
        
    def is_running(self):
        return self.run
        
    def stop_running(self):
        self.run=False

    def reset(self):
        self.grid=utils.LEVEL_1

    def is_pacman_alive(self):
        return self.pacman_alive

    def game_over(self):
        self.pacman_alive = False
        
    def is_win(self):
        return self.score == self.nbr_items
    
    def print_grid(self):
        for row in range(len(self.grid)):
            print(''.join(self.grid[row]))

    def start(self):
        while self.is_pacman_alive() and not self.is_win():
            self.next_state()
            self.print_grid()           
        return self.is_win()


    def next_state(self):
        mv_pacman = (0,0)
        mv_ghost = self.ghosts.getMoveGhost(self.grid, self.pacman_direction)
        self.apply_mv(mv_ghost,mv_pacman) 

    def apply_mv(self,g,p):
        #ATTENTION aux items quand un ghost va dessus = G
        pacman_oldpos = self.pacman_pos
        pacman_newpos = self.pacman_pos
        for i in range(len(g)):
            ghost_oldpos = g[i][0]
            ghost_newpos = g[i][1]

            if ghost_newpos == pacman_newpos or ( ghost_newpos == pacman_oldpos and pacman_newpos == ghost_oldpos ) :
                self.grid[ghost_oldpos[0]][ghost_oldpos[1]] = utils.EMPTY_CHAR
                self.grid[pacman_oldpos[0]][pacman_oldpos[1]] = utils.EMPTY_CHAR
                self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_CHAR
                self.game_over()
                return False
            elif self.grid[ghost_oldpos[0]][ghost_oldpos[1]]== utils.GHOST_ITEM_CHAR :
                self.grid[ghost_oldpos[0]][ghost_oldpos[1]] = utils.ITEM_CHAR
            else :
                self.grid[ghost_oldpos[0]][ghost_oldpos[1]] = utils.EMPTY_CHAR
                self.grid[pacman_oldpos[0]][pacman_oldpos[1]] = utils.EMPTY_CHAR
                
            if self.grid[ghost_newpos[0]][ghost_newpos[1]]== utils.ITEM_CHAR :
                self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_ITEM_CHAR
            elif self.grid[ghost_newpos[0]][ghost_newpos[1]]== utils.EMPTY_CHAR :
                self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_CHAR
                
            if self.grid[pacman_newpos[0]][pacman_newpos[1]]== utils.ITEM_CHAR :
                self.grid[pacman_newpos[0]][pacman_newpos[1]] = utils.PACMAN_CHAR
                self.score+=1
            elif self.grid[pacman_newpos[0]][pacman_newpos[1]]== utils.EMPTY_CHAR :
                self.grid[pacman_newpos[0]][pacman_newpos[1]] = utils.PACMAN_CHAR
                
            self.pacman_direction = utils.RIGHT
            
        
        

    
            
