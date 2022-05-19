from search import Search
import utils

class Ghost :
    def getMoveGhost(ghost_pos,grid):
        search = Search(ghost_pos,utils.PACMAN_CHAR,grid)
        return search.path[-1]
class Pacman :
    def getMovePacman(pacman_pos,grid):
        search = Search(pacman_pos,utils.ITEM_CHAR,grid)
        return search.path[-1]
