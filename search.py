import utils

class Node :
    def __init__(self,mvmt, pos, pr):
        self.mouvement = mvmt
        self.position = pos
        self.prev = pr
    
class Search :
    def __init__(self,start,target_char,grid):
        self.path= self.ghostSearch(start,target_char,grid)
        
    def ghostSearch(self,start, target_char,grid):
        node=self.breathFirst(start,target_char,grid)
        tab=[]
        while node.prev != None :
            tab.append(node.mouvement)
            node = node.prev
        return tab
        
    def breathFirst(self,start,target_char,grid):
        q=[Node(None,start,None)]
        while len(q) != 0 :
            current = q.pop(0)
            if grid[current.position[0]][current.position[1]] == target_char :
                return current
            for m in [utils.DOWN,utils.UP,utils.LEFT,utils.RIGHT]:
                new_pos = (current.position[0] + m[0] , current.position[1] + m[1])
                if grid[new_pos[0]][new_pos[1]] != utils.WALL_CHAR :
                    q.append(Node(m,new_pos,current))
        
