from n2_puzzle.puzzle import Direction, NPuzzle, animate_plan


def invalid_action(
    puzzle: NPuzzle, i: int, j: int, action: Direction, left_limit: int, up_limit: int
):
    """Check if for a given state of the puzzle, the action is valid or not

    For example if the puzzle state is:

    -----------------
    |  1| 15| 13| 12|
    -----------------
    | 14|   |  9|  8|
    -----------------
    | 10| 11|  6|  4|
    -----------------
    |  7|  3|  5|  2|
    -----------------

    And left is set to 1, then the action if left. Then even though
    the move is "legal", it won't be given this restriction.
    """
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


def move_diagonally_left(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Moves the target tile diagonally up left. It assumes that the
    blank tile is on the right of the target tile
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.UP,
        Direction.LEFT,
        Direction.DOWN,
        Direction.LEFT,
        Direction.UP,
        Direction.RIGHT,
    ]

    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, left_limit, up_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break


def move_up_left(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Moves the target tile upwards right. It assumes that the
    blank tile is on the right of the target tile
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.UP,
        Direction.LEFT,
        Direction.DOWN,
        Direction.RIGHT,
        Direction.UP,
    ]
    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, left_limit, up_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break


def move_diagonally_right(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Moves the target tile diagonally up right. It assumes that the
    blank tile is on the right of the target tile
    """
    i0, j0 = puzzle.tile_pos[0]
    plan = [
        Direction.LEFT,
        Direction.UP,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.RIGHT,
        Direction.UP,
    ]

    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, left_limit, up_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        i0, j0 = puzzle.tile_pos[0]
        if (i, j) == (it, jt):
            break


def move_up_right(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    This is used for the cases in which the target tile is
    on the last column. It assumes the blank tile will be
    on the left
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.UP,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.LEFT,
        Direction.UP,
    ]
    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, left_limit, up_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break
