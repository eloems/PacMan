from search import Search
import utils

class Pacman :
    def __init__(self,pos_pacman):
        self.pos = pos_pacman
        self.direction = None
        self.search = Search()

    def getMovePacman(self,grid):
        # Get the next movement
        mvnt = self.search.a_star(self.pos,grid)

        #apply the movement
        old_pos = self.pos
        self.pos = (old_pos[0] + mvnt[0], old_pos[1] + mvnt[1])
        self.direction = mvnt
        
        return [old_pos,self.pos]

    def setMovePacman(self,move,grid):
        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if grid[new_pos[0]][new_pos[1]] == utils.WALL_CHAR :
            return [self.pos,self.pos]
        
        old_pos = self.pos
        self.pos = new_pos
        self.direction = move
        return [old_pos,self.pos]

        
