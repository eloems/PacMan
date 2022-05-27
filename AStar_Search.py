import utils
import math
import heapq
import game





class AStar_Node:
    def __init__(self, mvmt, position, pr, parent=None):
        self.position = position
        self.parent = parent
        self.movement = mvmt
        self.prev = pr

        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    # def __repr__(self):
    #     return f"({self.position})"
    #
    # def __lt__(self, other):
    #     return self.f < other.f
    #
    # def __key(self):
    #     return self.position
    #
    # def __hash__(self):
    #     return hash(self.__key())
    #
    # def __eq__(self, other):
    #     if isinstance(other, AStar_Node):
    #         return self.__key() == other.__key()
    #     return NotImplemented

class AStar_Search:
    def __init__(self, args):
        self.best_path = []
        self.args = args
        self.moves = [utils.RIGHT, utils.DOWN,utils.LEFT, utils.UP]

    def reset_state(self):
        self.best_path = []

    def choose_next_move(self,state):
        grid, score, alive, pacman = state
        self.best_path = self.astar(state, self.game.target, interactive=True)

        # if self.best_path == "No path":
        #   print("A* did not find path")

        next_move = self.get_next_move(self.best_path, pacman)
        return next_move

    def get_next_move(self, path, pacman):
        next_node = path.pop()
        next_pos = next_node.position
        next_mov_bool = []

        for i in range(len(next_pos)):
            next_mov_bool.append(next_pos[i] - pacman[i])

        return next_mov_bool[:2]  #pas sur que ce soit 2

    # def choose_next_move(self, state):
    #
    #     grid, score, alive, pacman = state
    #
    #
    #
    # def get_next_move(self, path, pacman):
    #     next_node = path.pop()
    #     next_pos = next_node.position
    #     next_mov_bool = []
    #
    #     for i in range(len(next_pos)):
    #         next_mov_bool.append(next_pos[i] - pacman)
    #
    #actuellement Manhattan heuristic => distance euclidienne jusqu'à l'item
    def h_cost(self, current, end):
        res = math.sqrt(
            (current.position - end.position)**2
        )

    def in_grid(self, pos, grid):
        return 0 <= pos[0] < len(grid)




    def astar(self, state, target, interactive=False):

        grid, score, alive, pacman = state
        closed_list = set()
        open_list = []
        head_node = AStar_Node(pacman)
        goal_node = AStar_Node(target)

        heapq.heappush(open_list, head_node)

        while open_list:
            current_node = heapq.heappop(open_list)
            closed_list.add(current_node)

            if current_node == goal_node:
                path = []
                while current_node.parent is not None:
                    path.append(current_node)
                    current_node = current_node.parent

                # #je comprends pas le interactive dans le snake... je sais pas si c'est utile ou pas
                # if interactive:
                #     for j in path:
                #         self.game.grid[j.position] =

                for new_position in self.moves:
                    node_position = (current_node + new_position)

                    if not self.in_grid(node_position, grid):
                        continue
                    #
                    if grid[node_position[pacman]] == utils.WALL_CHAR:
                        continue

                    child = AStar_Node(node_position, current_node)

                    if child in closed_list:
                        continue

                    if (child in open_list
                            and open_list[open_list.index(child)].g <= current_node.g + 1):
                        continue

                    child.g = current_node.g + 1
                    child.h = self.h_cost(child, goal_node)
                    child.f = child.g + child.h
                    child.parent = current_node

                    heapq.heappush(open_list, child)

        return "No Path"







