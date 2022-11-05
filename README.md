# 8-puzzle-using-A\*-algorithm
8 Puzzle Problems:
An 8 puzzle is a simple game containing 9 squares divided into a grid of 3 by 3. It contains tiles from numbered 1 to 8 , so that each tile can be uniquely identified and one tile is empty. The purpose of the puzzle is to reach the goal state of the tile, from the initial state by moving individual tiles around the grid to the goal state.

 
![image](https://user-images.githubusercontent.com/22686539/200104457-455754e3-7081-4777-91e2-d59c9e318c44.png)

The above shows the transition of initial state to the goal state.

*Rules for solving the puzzle:*

We can move the empty tile with another tile in four possible directions i.e. up, down, left, right depending on the positions of the rest of the tiles. The empty space can take one step at a time and cannot move diagonally. We perform this process recursively until we get the final destination.

*A\* algorithm:*

A\* Search algorithm is one of the best and popular technique for finding path and graph traversal. It is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: it has a specific start point of a graph and its motto is to find a path cheapest path the given goal node. To do this, it keeps a track of all the nodes with its cost and select one at a time to explore further. It recursively perform this operation until it meets its termination criterion. 
At each step it generates children nodes based on the input and output given and it decides which children to explore further. It performs this operation based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes where f(n) = g(n) + h(n) where
      n is the next node on the path,
      g(n) is the cost of the path from the start node to n ,
      h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal.
  
This algorithm stops when it reached to goal node or it has no other goals which can be extended. The heuristic function is problem-specific. If the heuristic function is admissible, meaning that it never overestimates the actual cost to get to the goal, A* is guaranteed to return a least-cost path from start to goal.


*Properties:*

*Completeness:* 
1. On finite graphs with non-negative edge weights A* is guaranteed to terminate and is complete, i.e. it will always find a solution (a path from start to goal) if one exists. 
2. On infinite graphs with a finite branching factor and edge costs that are bounded away from zero A* is guaranteed to terminate only if there exists a solution. 
 Time: The time complexity will be O(b^d). 
 Space:  A* search keeps all the nodes in memory. The space complexity will be O(b^d). 
 Optimal: Yes, as A* will derive the path p from start to goal. The path p will be the shortest path and optimal as the nodes are expanded in order of increasing value of f(n) with increasing levels. The algorithm will discard the expansion of nodes where the value of f(n) is greater and gives output of shortest path.


*Heuristic Functions*

It provides an estimated cost to the goal from node n. Based on 
The two heuristic functions that we considered for solving 8-puzzle problem are: 
Misplaced Tile: The number of misplaced tiles calculated by comparing the current state and goal state.
 Manhattan Distance:  The distance between two tiles measured along the axes of right angles. It is the sum of absolute values of differences between goal state (i, j) coordinates and current state (l, m) coordinates respectively, i.e. |i - l|+ |j – m|.


![image](https://user-images.githubusercontent.com/22686539/200104555-c80c51d9-fe98-4de2-96d4-e632c785ce11.png)




