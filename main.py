from n2_puzzle.puzzle import NPuzzle, generate_template_board
from n2_puzzle.solver import State


def main():
    board = generate_template_board(4)
    puzzle = NPuzzle(board)
    print(puzzle)
    print(hash(puzzle))
    goal = NPuzzle(generate_template_board(4, is_goal=True))
    print(puzzle == goal)
    print(puzzle == NPuzzle(generate_template_board(4)))
    s = State(puzzle)
    print(s.neighbors())


if __name__ == "__main__":
    main()
