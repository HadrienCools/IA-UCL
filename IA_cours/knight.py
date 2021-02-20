# -*-coding: utf-8 -*
'''NAMES OF THE AUTHOR(S): Gael Aglin <gael.aglin@uclouvain.be>'''
import time
import sys
from search import *

#https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath

#################
# Problem class #
#################
class Knight(Problem):
    knight_moves=[(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-2,-1),(-2,1),(-1,-2)]

    def successor(self, state):
        moves_avalaible =[]
        for move in self.knight_moves:
            move_x = move[0]+state.pos[0]
            move_y = move[1]+state.pos[1]
            #print(move_x,move_y,state.nRows,state.nCols )
            
            if (move_x>=0 and move_y>=0 and move_x < state.nRows and move_y<state.nCols and  state.grid[move_x][move_y] != "♞"):
                
                moves_avalaible.append((move_x,move_y))
                
        #print(moves_avalaible,"moves_avalaible",state.visited_nb)
        for move_av in moves_avalaible: 
            #move_av
            newstate = State((state.nRows,state.nCols),move_av,visited_nb=state.visited_nb+1,actions = state.actions )
            yield(0,newstate)
            
    

    def goal_test(self, state):
        """
        """
        #pass
        goal_flag =  False 
        opimal_moves_nb = state.nCols * state.nRows
        if(state.visited_nb ==opimal_moves_nb ):
            goal_flag = True 
        return goal_flag
        


###############
# State class #
###############
class State:
    def __init__(self, shape, init_pos, visited_nb=1, actions=[]):
        print(actions)
        self.nRows = shape[0]
        self.nCols = shape[1]
        self.grid = []
        for i in range(self.nRows):
            self.grid.append([" "]*self.nCols)
        self.grid[init_pos[0]][init_pos[1]] = "♘"
        self.pos = init_pos
        self.visited_nb = visited_nb
        self.moves(actions)
        self.actions = actions
        self.actions.append(init_pos)
#        self.grid_val = []
#        for i in range(self.nRows):
#            self.grid_val.append([])
#            for j in range(self.nCols):
#                if i == init_pos[0] and j == init_pos[1]:
#                    self.grid_val[i].append(2)
#                else:
#                    self.grid_val[i].append(0)
    
    def moves(self, moves):
        #yo = []
        #print("fdshjnfsdfsd",yo)
        for i in range(len(moves)):
            self.grid[moves[i][0]][moves[i][1]] = "♞"

    def __str__(self):
        n_sharp = 2 * self.nCols + 1
        s = ("#" * n_sharp) + "\n"
        for i in range(self.nRows):
            s += "#"
            for j in range(self.nCols):
                s = s + str(self.grid[i][j]) + " "
            s = s[:-1]
            s += "#"
            if i < self.nRows - 1:
                s += '\n'
        s += "\n"
        s += "#" * n_sharp
        return s
"""   
class State:

    def __init__(self, shape, init_pos,visited_nb = 0,moves=[]):
        self.nRows = shape[0]
        self.nCols = shape[1]
        self.grid = []
        for i in range(self.nRows):
            self.grid.append([" "]*self.nCols)
        self.grid[init_pos[0]][init_pos[1]] = "♘"
        #
        #?
        self.visited_nb = 0
        self.moves = []
        self.pos = init_pos
        
        #self.position = init_pos
    # mutateur appelés par night qui vont modif les variable d etat 
    def __str__(self):
        n_sharp = 2 * self.nCols + 1
        s = ("#" * n_sharp) + "\n"
        for i in range(self.nRows):
            s += "#"
            for j in range(self.nCols):
                s = s + str(self.grid[i][j]) + " "
            s = s[:-1]
            s += "#"
            if i < self.nRows - 1:
                s += '\n'
        s += "\n"
        s += "#" * n_sharp
        return s"""


##############################
# Launch the search in local #
##############################
#Use this block to test your code in local
# Comment it and uncomment the next one if you want to submit your code on INGInious
with open('instances.txt') as f:
    instances = f.read().splitlines()

for instance in instances:
    elts = instance.split(" ")
    shape = (int(elts[0]), int(elts[1]))
    init_pos = (int(elts[2]), int(elts[3]))
    print(init_pos)
    init_state = State(shape, init_pos)
    print(init_state.grid)

    problem = Knight(init_state)

    # example of bfs tree search
    startTime = time.perf_counter()
    #node, nb_explored, remaining_nodes = breadth_first_graph_search(problem)
    node, nb_explored, remaining_nodes = depth_first_tree_search(problem)
    endTime = time.perf_counter()

    # example of print
    path = node.path()
    path.reverse()

    print('Number of moves: ' + str(node.depth))
    for n in path:
        print(n.state)  # assuming that the __str__ function of state outputs the correct format
        print()
    print("* Execution time:\t", str(endTime - startTime))
    print("* Path cost to goal:\t", node.depth, "moves")
    print("* #Nodes explored:\t", nb_explored)
    print("* Queue size at goal:\t",  remaining_nodes)



####################################
# Launch the search for INGInious  #
####################################
#Use this block to test your code on INGInious
shape = (int(sys.argv[1]),int(sys.argv[2]))
init_pos = (int(sys.argv[3]),int(sys.argv[4]))
init_state = State(shape, init_pos)

problem = Knight(init_state)

# example of bfs tree search
startTime = time.perf_counter()
node, nb_explored, remaining_nodes = breadth_first_graph_search(problem)
endTime = time.perf_counter()

# example of print
path = node.path()
path.reverse()

print('Number of moves: ' + str(node.depth))
for n in path:
    print(n.state)  # assuming that the __str__ function of state outputs the correct format
    print()
print("* Execution time:\t", str(endTime - startTime))
print("* Path cost to goal:\t", node.depth, "moves")
print("* #Nodes explored:\t", nb_explored)
print("* Queue size at goal:\t",  remaining_nodes)
