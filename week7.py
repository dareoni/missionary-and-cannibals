class State:
    def __init__(self, missionaries, cannibals, boat_on_left):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_on_left = boat_on_left

    def is_valid_state(self):
        # Check if the state is valid (i.e., no missionaries are eaten)
        if self.missionaries < 0 or self.missionaries > 3 or self.cannibals < 0 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if self.missionaries < 3 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True

def get_possible_next_states(current_state):
    next_states = []
    boat_positions = [True, False] if current_state.boat_on_left else [False, True]

    for num_missionaries in range(3 + 1):
        for num_cannibals in range(3 + 1):
            for boat_on_left in boat_positions:
                if num_missionaries + num_cannibals >= 1 and num_missionaries + num_cannibals <= 2:
                    new_state = State(
                        current_state.missionaries + (num_missionaries if current_state.boat_on_left else -num_missionaries),
                        current_state.cannibals + (num_cannibals if current_state.boat_on_left else -num_cannibals),
                        boat_on_left
                    )
                    if new_state.is_valid_state():
                        next_states.append(new_state)

    return next_states

def dfs_search(current_state, path, visited_states):
    path.append(current_state)

    if current_state.missionaries == 0 and current_state.cannibals == 0 and not current_state.boat_on_left:
        return True  # Goal state found

    visited_states.add((current_state.missionaries, current_state.cannibals, current_state.boat_on_left))

    next_states = get_possible_next_states(current_state)
    for next_state in next_states:
        if (next_state.missionaries, next_state.cannibals, next_state.boat_on_left) not in visited_states:
            if dfs_search(next_state, path, visited_states):
                return True

    path.pop()
    return False

def solve_problem(missionaries, cannibals, boat_on_left):
    start_state = State(missionaries, cannibals, boat_on_left)
    path = []
    visited_states = set()

    if dfs_search(start_state, path, visited_states):
        return path
    else:
        return None

def print_solution(path):
    if path is None:
        print("No solution found.")
    else:
        print("Series of Crossings to Get Everyone Safely to the Other Side:")
        for state in path:
            print(f"Missionaries: {state.missionaries}, Cannibals: {state.cannibals}, Boat on left: {state.boat_on_left}")
        print("\n")

# Solve the problem and print the solution
solution_path = solve_problem(3,4,False)
print_solution(solution_path)

solution_path = solve_problem(4,4,False)
print_solution(solution_path)
