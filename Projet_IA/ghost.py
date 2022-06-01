from search import Search
import random
import utils

class Ghost :
    def __init__(self,tab_pos):
        
        # tab_pos = the postions of all the ghosts , self.ghosts is a dictionary with the key = number of the ghost and value = position of this ghost.
        self.ghosts = {}
        for i in range(len(tab_pos)):
            self.ghosts[i+1] = tab_pos[i]
        # the instance of the class Search for "communication" between ghosts
        self.searchPacman=Search()

    # This function return a list of lists for every ghosts with the old_pos and new_pos. It call the right search function to get the movement of the ghosts   
    def getMoveGhost(self,grid,direction):
        ghosts_old_new_pos = []

        for i in range(len(self.ghosts)):
            idx =i+1
            if idx == 1 :
                ghosts_old_new_pos.append(self.getMoveGhost1(grid))
            elif idx == 2 and self.searchPacman.node_pacman != None and direction != None:
                ghosts_old_new_pos.append(self.getMoveGhost2(direction,grid))

        return ghosts_old_new_pos

    # This function return a list with the old position qnd the new position of the ghost.It is the comportement of the first ghost. The ghost targets directly the pacman
    def getMoveGhost1(self,grid):
        ghost_pos = self.ghosts[1]
        path = self.searchPacman.ghostSearch(ghost_pos,utils.PACMAN_CHAR,grid)
        
        #get the first movement to do thanks of the backtraking and apply it
        mvnt = path[-1]
        new_pos = (ghost_pos[0] + mvnt[0], ghost_pos[1] + mvnt[1])
        self.ghosts[1] = new_pos
        return [ghost_pos,new_pos]

    # This function return a list with the old position qnd the new position of the ghost.It is the comportement of the second ghost. The ghost targets three tiles after the position of the pacman ( in the same direction)
    def getMoveGhost2(self,direction,grid):
        ghost_pos = self.ghosts[2]

        # Get the current position of pacman thanks to the instance of Search and the search of the first Ghost
        current_targetPos = self.searchPacman.node_pacman.position

        # Get the position pacman +3
        tile=0
        while tile != 3 :
            new_current_pos = (current_targetPos[0] + direction[0],current_targetPos[1] + direction[1])
            if grid[new_current_pos[0]][new_current_pos[1]] == utils.WALL_CHAR :
                direct_list = [utils.DOWN,utils.UP,utils.LEFT,utils.RIGHT]
                direct_list.remove(direction)
                random.shuffle(direct_list)
                direction = direct_list[0]
            else :
                current_targetPos = new_current_pos
                tile += 1
        # If the ghost is over the position +3 , then not move , else do the search   
        not_move = current_targetPos == ghost_pos       
        mvnt = (0,0)
        if not not_move :
            path = self.searchPacman.ghostSearch(ghost_pos,current_targetPos,grid)
            mvnt = path [-1]
        new_pos = (ghost_pos[0] + mvnt[0], ghost_pos[1] + mvnt[1])
        self.ghosts[2] = new_pos
        return [ghost_pos,new_pos]            
                
