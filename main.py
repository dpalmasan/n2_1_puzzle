from n2_puzzle.puzzle import NPuzzle, animate_plan, generate_template_board
from n2_puzzle.search import State, a_star_puzzle


def main():
    board = generate_template_board(3)
    puzzle = NPuzzle(board)
    goal = NPuzzle(generate_template_board(3, is_goal=True))
    plan = a_star_puzzle(State(puzzle), State(goal))
    animate_plan(puzzle, plan)


if __name__ == "__main__":
    main()
