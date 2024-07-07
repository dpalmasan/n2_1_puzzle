import argparse
from typing import Union

from n2_puzzle.puzzle import (
    Direction,
    NPuzzle,
    animate_plan,
    draw_puzzle,
    generate_template_board,
)
from n2_puzzle.solver import solve_puzzle

GOD_MODE = "god"

parser = argparse.ArgumentParser(
    prog="NPuzzleSolver",
    description="Given a integer generates the N^2 - 1 puzzle and solves it",
    epilog="Enjoy!",
)

parser.add_argument("--n", type=int, default=3, help="Puzzle dimension")


def is_valid_move(puzzle: NPuzzle, tile: Union[str, int]) -> bool:
    assert type(tile) == int
    limit_value = puzzle.n**2 - 1
    if not 0 <= tile <= limit_value:
        return False

    ti, tj = puzzle.tile_pos[tile]
    bi, bj = puzzle.tile_pos[0]
    return bi == ti - 1 or bi == ti + 1 or bj == tj - 1 or bj == tj + 1


def player_move(puzzle: NPuzzle, tile: int) -> None:
    ti, tj = puzzle.tile_pos[tile]
    bi, bj = puzzle.tile_pos[0]
    if bi == ti - 1:
        dir = Direction.DOWN

    elif bi == ti + 1:
        dir = Direction.UP
    elif bj == tj - 1:
        dir = Direction.RIGHT
    else:
        dir = Direction.LEFT

    animate_plan(puzzle, [dir])


def player_input(puzzle: NPuzzle) -> Union[str, int]:
    tile_input: Union[str, int] = ""
    while type(tile_input) != int or not is_valid_move(puzzle, tile_input):
        tile_input = input("Input tile to move: ")
        try:
            tile_input = int(tile_input)
        except ValueError:
            assert type(tile_input) == str
            if tile_input.lower() == GOD_MODE:
                tile_input = GOD_MODE
                break

    return tile_input


def puzzle_is_complete(puzzle: NPuzzle) -> bool:
    goal_puzzle = NPuzzle(generate_template_board(puzzle.n, is_goal=True))
    return puzzle == goal_puzzle


def main():
    args = parser.parse_args()
    n = args.n

    # TODO: Add support for n == 9
    assert 3 <= n <= 8, f"Unsupported n: {n}"

    puzzle = NPuzzle(generate_template_board(n))
    draw_puzzle(puzzle)
    while not puzzle_is_complete(puzzle):
        tile_to_move = player_input(puzzle)
        if tile_to_move == GOD_MODE:
            print("Activating GOD MODE!")
            input("Press any key to continue...")
            solve_puzzle(puzzle)
            continue

        player_move(puzzle, tile_to_move)

    print("Puzzle was solved!")


if __name__ == "__main__":
    main()
