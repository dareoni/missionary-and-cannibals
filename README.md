# missionary-and-cannibals

This code provides a solution to the famous "Missionaries and Cannibals" problem using depth-first search (DFS). The problem involves moving a group of missionaries and cannibals 
across a river using a boat that can carry a maximum of two people. 
The goal is to transport everyone to the other side of the river without ever leaving more 
cannibals than missionaries on either side of the river, as the cannibals would eat the missionaries.

Let's break down the code step by step:

1. `State` class: This class represents the current state of the problem, including the number of missionaries, cannibals, and the boat's position (whether it's on the left or right side of the river). It also contains a method `is_valid_state()` that checks if the current state is valid (no missionaries are eaten).

2. `get_possible_next_states()` function: This function generates a list of possible next states from the current state. It considers all combinations of moving 1 or 2 missionaries and/or cannibals to the other side of the river.

3. `dfs_search()` function: This function performs a depth-first search to find a valid sequence of moves that leads to the goal state (all missionaries and cannibals on the other side). It uses recursion to explore different states and backtracks if a dead end is reached.

4. `solve_problem()` function: This function initializes the starting state and uses the `dfs_search()` function to find a solution. It returns a list of states representing the sequence of moves needed to solve the problem or `None` if no solution is found.

5. `print_solution()` function: This function prints the solution path if a solution is found or a message indicating that no solution exists.

6. Solving the problem: The code calls the `solve_problem()` function twice, first with 3 missionaries and 4 cannibals on the left side and then with 4 missionaries and 4 cannibals on the left side. It prints the solution paths using the `print_solution()` function.

7. Execution and Output: The code solves the "Missionaries and Cannibals" problem for the provided scenarios and prints the steps required to move all individuals safely to the other side of the river.

This code provides a clear implementation of the solution to the "Missionaries and Cannibals" problem using depth-first search. It's a good example of how to represent and solve a simple problem using Python and basic algorithmic techniques. It can be used as a reference for understanding and implementing similar problems or as a demonstration of DFS in action.
