from ghost import Ghost
from ghost import Pacman

import utils

class Game:
    def __init__(self):
        self.run = True
        self.grid = utils.LEVEL_1
        self.pacman_alive=True
        self.pacman_pos = self.init_pos(utils.PACMAN_CHAR)
        self.ghost_pos = self.init_pos(utils.GHOST_CHAR)
        self.score = 0
        self.nbr_items = self.init_nbr_items()
        
    def init_pos(self,target_char):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == target_char :
                    return (row,col)
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
        mv_ghost = Ghost.getMoveGhost(self.ghost_pos,self.grid)
        mv_pacman = Pacman.getMovePacman(self.pacman_pos,self.grid)
        self.apply_mv(mv_ghost,mv_pacman) 

    def apply_mv(self,g,p):
        #ATTENTION aux items quand un ghost va dessus = G
        
        ghost_newpos = ( self.ghost_pos[0] + g[0] , self.ghost_pos[1] + g[1] )
        pacman_newpos = ( self.pacman_pos[0] + p[0] , self.pacman_pos[1] + p[1] )

        if ghost_newpos == pacman_newpos or ( ghost_newpos == self.pacman_pos and pacman_newpos == self.ghost_pos ) :
            self.grid[self.ghost_pos[0]][self.ghost_pos[1]] = utils.EMPTY_CHAR
            self.grid[self.pacman_pos[0]][self.pacman_pos[1]] = utils.EMPTY_CHAR
            self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_CHAR
            self.game_over()
            return False
        elif self.grid[self.ghost_pos[0]][self.ghost_pos[1]]== utils.GHOST_ITEM_CHAR :
            self.grid[self.ghost_pos[0]][self.ghost_pos[1]] = utils.ITEM_CHAR
        else :
            self.grid[self.ghost_pos[0]][self.ghost_pos[1]] = utils.EMPTY_CHAR
            self.grid[self.pacman_pos[0]][self.pacman_pos[1]] = utils.EMPTY_CHAR
            
        if self.grid[ghost_newpos[0]][ghost_newpos[1]]== utils.ITEM_CHAR :
            self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_ITEM_CHAR
        elif self.grid[ghost_newpos[0]][ghost_newpos[1]]== utils.EMPTY_CHAR :
            self.grid[ghost_newpos[0]][ghost_newpos[1]] = utils.GHOST_CHAR
            
        if self.grid[pacman_newpos[0]][pacman_newpos[1]]== utils.ITEM_CHAR :
            self.grid[pacman_newpos[0]][pacman_newpos[1]] = utils.PACMAN_CHAR
            self.score+=1
        elif self.grid[pacman_newpos[0]][pacman_newpos[1]]== utils.EMPTY_CHAR :
            self.grid[pacman_newpos[0]][pacman_newpos[1]] = utils.PACMAN_CHAR
        self.pacman_pos = pacman_newpos
        self.ghost_pos = ghost_newpos
            
        
        

    
            
