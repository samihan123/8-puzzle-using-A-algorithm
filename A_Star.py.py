# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 01:28:43 2021

@author: sjawalka
"""
from copy import deepcopy

goal_state = []
close_list = []
open_list = []
node_generated = 0


###########################################################################
# Node class would contain, structure of a 8-puzzle
############################################################################
class Node:
    """

    :type value: array
    :param value: 3 x 3 array having 8-puzzle
    :type h: int
    :param h: Heuristic function value estimated cost to goal state from current state
    :type g: int
    :param g: Cost so far to reach current state from the initial state
    :type fn: int
    :param fn: The sum of h and g
    :type parent: Node
    :param parent: Reference of parent of Node
    :type children: array of Node
    :param children: References of Children of the Node
    """

    def __init__(self, value=None, h=0, g=0, fn=0, parent=None, children=[]):
        self.value = value
        self.h = h
        self.g = g
        self.fn = fn
        self.parent = parent
        self.children = children

    ######################################################################
    # function to calculate g(n) ; it would incremented at each position
    ######################################################################
    def set_g(self):
        try:
            self.g = self.parent.g + 1
        except Exception as e:
            print("Error while setting g, ", str(e))

    ######################################################################
    # calculate first heuristic function; calculate no. of misplace tiles
    ######################################################################
    def get_h1(self):
        try:
            h1_count = 0
            for i in range(len(self.value)):
                for j in range(len(self.value[i])):
                    if self.value[i][j] != 0 and self.value[i][j] != goal_state[i][j]:
                        h1_count += 1
            return h1_count
        except Exception as e:
            print("Error while getting h1 value ", str(e))

    ######################################################################
    # calculate second heuristic function, calculate no. of moves require for
    # single tile ie manhattan distance
    ######################################################################
    def get_h2(self):
        try:
            h2_dist = 0
            for i in range(len(self.value)):
                for j in range(len(self.value[i])):
                    if self.value[i][j] != 0 and self.value[i][j] != goal_state[i][j]:
                        # getting the right position in goal state of misplace element
                        x, y = get_position(goal_state, self.value[i][j])
                        h2_dist = h2_dist + (abs(x - i) + abs(y - j))
            return h2_dist
        except Exception as e:
            print("Error while getting h2 value ", str(e))

    #######################################################################
    # get h heuristic function, it would be h1 or h2 as per user input
    #######################################################################
    def set_h(self, h_choice):
        try:
            if h_choice == 1:
                self.h = self.get_h1()
            elif h_choice == 2:
                self.h = self.get_h2()
        except Exception as e:
            print("Error while setting h value", str(e))

    #######################################################################
    # get fn = g + h
    #######################################################################
    def set_fn(self):
        try:
            self.fn = self.g + self.h
        except Exception as e:
            print("Error while setting fn ", str(e))

    #######################################################################
    # check if node is the goal
    #######################################################################
    def is_goal(self):
        try:
            return self.value == goal_state
        except Exception as e:
            print("Error while checking the goal, ", str(e))

    ########################################################################
    # generate children, create possibilities from given node
    ########################################################################
    def generate_children(self, h_choice):

        try:
            children = []
            # get the previous array
            prev_arr = self.value
            x, y = get_position(prev_arr, 0)

            # list of tuples consisting new moves index
            index_array = []

            # generating moves
            x1 = x + 1
            y1 = y + 1
            x2 = x - 1
            y2 = y - 1
            # checking valid moves and storing it in tuple and appending to array
            if -1 < x1 < 3:
                index_array.append((x1, y))
            if -1 < y1 < 3:
                index_array.append((x, y1))

            if -1 < x2 < 3:
                index_array.append((x2, y))

            if -1 < y2 < 3:
                index_array.append((x, y2))

            for tup_index in index_array:
                p = Node()
                p.value = deepcopy(prev_arr)
                # swapping 0 and new position
                p.value[tup_index[0]][tup_index[1]], p.value[x][y] = p.value[x][y], p.value[tup_index[0]][tup_index[1]]
                # calculating all the values of child
                p.parent = self
                p.set_g()
                p.set_h(h_choice)
                p.set_fn()
                global node_generated
                node_generated = node_generated + 1
                children.append(p)
            self.children = children
        except Exception as e:
            print("Error occurred in generate children ", str(e))


########################################################################
# get input
#########################################################################
def get_input():
    try:
        matrix = []
        for i in range(3):
            row = list(map(int, input().split()))
            matrix.append(row)
        return matrix
    except Exception as e:
        print("Error occurred in getting input", str(e))


########################################################################
# get output
# param - array, row , column,
# output - display matrix
#########################################################################
def get_output(array, row, column, f=None):
    try:
        for i in range(row):
            print("\n", file=f)
            for j in range(column):
                print(array[i][j], end=" ", file=f)
        print("\n", file=f)
    except Exception as e:
        print("Error occurred while getting output ", str(e))


######################################################################
# get x ,y  position of given array for given values
#######################################################################
def get_position(array, value):
    try:
        y = -1
        x = -1
        for i in range(len(array)):
            try:
                # find the index of value in array
                y = (array[i].index(value))
                x = i
                break
            except:
                # exception would occurs if index value is not found in the
                # row
                continue
        return x, y
    except Exception as e:
        print("Error while getting position, ", str(e))


######################################################################
# A * Algorithm function
#######################################################################
def a_star_algo(node, h_choice):
    try:
        open_list.append(node)

        while len(open_list) != 0:
            # find the lowest fn value in open list
            min_fn_node = min(open_list, key=lambda n: n.fn)
            # pop/remove that node from the frontier
            open_list.remove(min_fn_node)

            # goal check
            if min_fn_node.is_goal():
                return min_fn_node

            # generate children
            min_fn_node.generate_children(h_choice)

            # iterate through all the children
            for child in min_fn_node.children:
                # if same child.value is present in open list,
                # check for their f, if child has greater f then skip
                dupl_child_open = list(filter(lambda o: o.value == child.value, open_list))
                if len(dupl_child_open) > 0:
                    if dupl_child_open[0].fn < child.fn:
                        continue

                # if same child.value is present in close list,
                # check of their f, if child has greater f then skip
                dupl_child_close = list(filter(lambda o: o.value == child.value, close_list))
                if len(dupl_child_close) > 0:
                    if dupl_child_close[0].fn < child.fn:
                        continue

                # add child node to open list
                open_list.append(child)

            # add parent to close list
            close_list.append(min_fn_node)

    except Exception as e:
        print("Got exception in A* function", e)


def is_valid_input(initial_state, goal_state):
    # edge case check of valid state, check if we do not have duplicate number
    # in array
    for ar in initial_state:
        if len(set(ar)) != len(ar):
            return False
    for ar in goal_state:
        if len(set(ar)) != len(ar):
            return False
    # check if empty space is present
    x, y = get_position(initial_state, 0)
    if x == -1:
        print("Empty space not found in the initial state")
        return False
    x, y = get_position(goal_state, 0)
    if x == -1:
        print("Empty space not found in the goal state")
        return False
    return True


######################################################################
# This function checks if given 8 puzzle problem has a solution
# with respect to given goal state
#######################################################################
def is_problem_solvable(initial_state, goal_state):
    try:
        # flatten the list
        initial_state_ls = [item for ls in initial_state for item in ls if item != 0]
        initial_state_inv_count = 0
        goal_state_ls = [item for ls in goal_state for item in ls if item != 0]
        goal_state_inv_count = 0

        # add all inv pairs present in initial_state
        for i in range(0, len(initial_state_ls) - 1):
            for j in range(i + 1, len(initial_state_ls)):
                if initial_state_ls[i] > initial_state_ls[j]:
                    initial_state_inv_count += 1

        # add all inv pairs present in goal_state
        for i in range(0, len(goal_state_ls) - 1):
            for j in range(i + 1, len(goal_state_ls)):
                if goal_state_ls[i] > goal_state_ls[j]:
                    goal_state_inv_count += 1

        # check the parity
        if (initial_state_inv_count % 2) == goal_state_inv_count % 2:
            return True
        else:
            return False
    except Exception as e:
        print("Error while checking if problem has solution,", str(e))


######################################################################
# main function
#######################################################################
def main():
    try:
        print("A* function")
        print("Enter 3*3 initial state array, put 0  for empty space.")
        root_array = get_input()

        print("Enter 3*3 goal state array, put 0 for empty space.")
        global goal_state
        goal_state = get_input()

        # check if the input is valid
        if not is_valid_input(root_array, goal_state):
            print("Input is invalid! Please try again.")
            return -1

        # check if the problem state is solvable
        if not is_problem_solvable(root_array, goal_state):
            print("The given problem does not have solution!")
            return -1

        h_choice = int(input("Enter heuristic of your choice \n1)Misplaced tiles\n2)Manhattan distance "))

        # creating root node
        root = Node(root_array)
        global node_generated
        node_generated = node_generated + 1
        print("A * algorithm Started,you would get to your goal through optimal path!!!")
        output_node = a_star_algo(root, h_choice)
        print("Output state - :")
        get_output(output_node.value, 3, 3)

        final_array = []
        node = output_node
        while node.parent is not None:
            # print(node.value)
            final_array.append(node.value)
            node = node.parent
        final_array.append(node.value)

        with open('output_A-star.txt', 'w', encoding="utf-8") as f:
            if len(final_array) < 20:
                f = None
            else:
                print("Please check the detailed output in output_A-star.txt")
            print("Path we traveled is", file=f)
            for i in range(len(final_array) - 1, 0, -1):
                get_output(final_array[i], 3, 3, f)
                print("  \u2193", file=f)
            get_output(final_array[0], 3, 3, f)

            print("\nTotal path cost required for the give solution is {}".format(output_node.fn), file=f)
            print("Total Nodes generated = {}".format(node_generated), file=f)
            print("Total Nodes expanded = {}".format(len(close_list)), file=f)
    except Exception as e:
        print("Error in main, ", str(e))


######################################################################
# calling main function
#######################################################################
main()
