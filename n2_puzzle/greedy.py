from n2_puzzle.puzzle import Direction, NPuzzle


def invalid_action(
    puzzle: NPuzzle, i: int, j: int, action: Direction, left_limit: int, up_limit: int
):
    n = puzzle.n
    return (
        action == Direction.LEFT
        and j == left_limit
        or action == Direction.RIGHT
        and j == n - 1
        or action == Direction.UP
        and i == up_limit
        or action == Direction.DOWN
        and i == n - 1
    )
