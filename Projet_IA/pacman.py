from search import Search

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

        
