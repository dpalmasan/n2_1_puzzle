import argparse

from n2_puzzle.puzzle import NPuzzle, generate_template_board
from n2_puzzle.solver import solve_puzzle

parser = argparse.ArgumentParser(
    prog="NPuzzleSolver",
    description="Given a integer generates the N^2 - 1 puzzle and solves it",
    epilog="Enjoy!",
)

parser.add_argument("--n", type=int, default=3, help="Puzzle dimension")


def main():
    args = parser.parse_args()
    n = args.n

    # TODO: Add support for n == 9
    assert 3 <= n <= 8, f"Unsupported n: {n}"
    puzzle = NPuzzle(generate_template_board(n))
    solve_puzzle(puzzle)


if __name__ == "__main__":
    main()
