from n2_puzzle.greedy import process_column, process_row
from n2_puzzle.puzzle import NPuzzle, animate_plan, generate_template_board
from n2_puzzle.search import State, a_star_puzzle


def solve_puzzle(puzzle: NPuzzle):
    n = puzzle.n
    for i in range(n):
        if n == 3:
            break
        it = i
        jt = i
        start_value = jt * puzzle.n + jt + 1
        process_row(puzzle, it, start_value)
        process_column(puzzle, jt, start_value)
        n -= 1

    # Extract sub-puzzle to solve
    puzzle_init_state = []
    for row in puzzle.board[-3:]:
        puzzle_init_state.append(row[-3:])
    init_state = State(NPuzzle(puzzle_init_state))
    puzzle_goal = generate_template_board(puzzle.n, is_goal=True)
    puzzle_goal_reduced = []

    # Create the goal state
    for row in puzzle_goal[-3:]:
        puzzle_goal_reduced.append(row[-3:])
    goal_state = State(NPuzzle(puzzle_goal_reduced))
    plan = a_star_puzzle(init_state, goal_state)
    animate_plan(puzzle, plan)
