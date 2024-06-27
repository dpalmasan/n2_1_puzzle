# from n2_puzzle.search import State, a_star_puzzle
from n2_puzzle.greedy import process_row
from n2_puzzle.puzzle import NPuzzle, generate_template_board


def main():
    board = generate_template_board(4)
    puzzle = NPuzzle(board)
    process_row(puzzle, 0, 1)


if __name__ == "__main__":
    main()
