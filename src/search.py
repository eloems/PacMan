import utils

class Node :
    def __init__(self,mvmt, pos, pr , ancestor_tab, type_search = 1,d_item = 0, d_ghost = 0):
        self.mouvement = mvmt
        self.position = pos
        self.prev = pr
        self.pos_ancestor= ancestor_tab

        if type_search == 2:
            self.g = d_item
            self.h = d_ghost
            self.f = self.g - self.h
        
    
class Search :
    def __init__(self):
        self.node_pacman=None
        
    def ghostSearch(self,start,target,grid):
        node = Node(None,start,None , [])
        node= self.breadthFirst(node,[target],grid)

        #if it is the first ghost search, then set the position of the pacman fort the other ghost.
        if type(target)== str :
            self.node_pacman=node
        return self.get_path(node)
        
    def breadthFirst(self,start,target,grid):
        q=[start]
        while len(q) != 0 :
            current = q.pop(0)
            # Check if the target is a str ( CHAR ) or a position ( tuple )
            type_target = type(target[0])== str
            
            # If the current node is the target then return it
            if type_target :
                if grid[current.position[0]][current.position[1]] in target:
                    return current
            else :
                if current.position in target :
                    return current
            # Check for the next movements possible from the current node and if this is not a wall and not visited yet , append the new Node corresponding to the agenda
            for m in [utils.DOWN,utils.UP,utils.LEFT,utils.RIGHT]:
                new_pos = (current.position[0] + m[0] , current.position[1] + m[1])
                if grid[new_pos[0]][new_pos[1]] != utils.WALL_CHAR and not(new_pos in current.pos_ancestor) :
                    q.append(Node(m,new_pos,current,current.pos_ancestor + [current.position]))
                    
    # This function return  list of movement. It is the backtraking from the node of the target (in parameter).                
    def get_path(self,node_target):
        tab=[]
        while node_target.prev != None :
            tab.append(node_target.mouvement)
            node_target = node_target.prev
        return tab
        
    def a_star(self,start,grid):
        mvmt = [utils.DOWN, utils.UP, utils.LEFT, utils.RIGHT]
        q = []
        for m in mvmt :
            pos = ( start[0] + m[0] , start[1] + m[1] )
            # Add the node of the movement only if the movement does'nt go to wall
            if grid[pos[0]][pos[1]] != utils.WALL_CHAR :
                node_start = Node(None,pos,None,[])
                # Get the shortest path to a item from the new position = g()
                node_target_item = self.breadthFirst(node_start,[utils.ITEM_CHAR],grid)
                g_function = len(self.get_path(node_target_item))

                # Get the shortest path to a ghost from the new position = h()
                node_target_ghost = self.breadthFirst(node_start,[utils.GHOST_ITEM_CHAR,utils.GHOST_CHAR,utils.GHOST_GHOST_CHAR],grid)
                h_function = len(self.get_path(node_target_ghost))

                # Force to not go on a ghost even if the item is very very close
                if h_function <=1 :
                    h_function = -100

                new_node = Node(m,pos,None,None,2,g_function,h_function)
                q.append(new_node)
                
        selected_node = self.get_minimum_function_node(q)
        return selected_node.mouvement
    
    def get_minimum_function_node(self,q):
        min_function_node = q[0]
        for i in range(len(q)):
            if min_function_node.f > q[i].f :
                min_function_node = q[i]
        return min_function_node
        
                

