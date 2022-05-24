import utils

class Node :
    def __init__(self,mvmt, pos, pr , ancestor_tab):
        self.mouvement = mvmt
        self.position = pos
        self.prev = pr
        self.pos_ancestor= ancestor_tab
    
class Search :
    def __init__(self):
        self.node_pacman=None
        
    def ghostSearch(self,start,target,grid):
        node = Node(None,start,None , [])
        node= self.breadthFirst(node,target,grid)


        if type(target)== str :
            self.node_pacman=node
        tab=[]
        while node.prev != None :
            tab.append(node.mouvement)
            node = node.prev
        return tab
        
    def breadthFirst(self,start,target,grid):
        q=[start]
        while len(q) != 0 :
            current = q.pop(0)        
            type_target = type(target)== str
            if type_target :
                if grid[current.position[0]][current.position[1]] == target:
                    return current
            else :
                if current.position == target :
                    return current
            for m in [utils.DOWN,utils.UP,utils.LEFT,utils.RIGHT]:
                new_pos = (current.position[0] + m[0] , current.position[1] + m[1])
                if grid[new_pos[0]][new_pos[1]] != utils.WALL_CHAR and not(new_pos in current.pos_ancestor) :
                    q.append(Node(m,new_pos,current,current.pos_ancestor + [current.position]))
        
