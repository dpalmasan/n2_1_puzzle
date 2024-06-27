from n2_puzzle.puzzle import NPuzzle, generate_template_board


def main():
    board = generate_template_board(4)
    puzzle = NPuzzle(board)
    print(puzzle)


if __name__ == "__main__":
    main()
