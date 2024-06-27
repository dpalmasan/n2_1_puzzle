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


def move_blank_to_target(puzzle: NPuzzle, target_tile: int, it: int, jt: int):
    """
    Moves the blank tile so it is next to the target tile
    """
    # Corner case in which the target position is at the end
    # and the target tile is as well at the end
    # In this case the blank will be on the left of the target
    i0, j0 = puzzle.tile_pos[0]
    i, j = puzzle.tile_pos[target_tile]

    if (i, j) == (it, jt):
        return

    if jt == puzzle.n - 1 and j == puzzle.n - 1:
        if j0 == j:
            action = Direction.LEFT
            animate_plan(puzzle, [action])
        else:
            while j0 != j - 1:
                action = Direction.RIGHT
                animate_plan(puzzle, [action])
                i0, j0 = puzzle.tile_pos[0]
    else:
        # In any other case we just move the blank
        # right next to the target
        while j0 != j + 1:
            if j == puzzle.n - 1 and j0 == puzzle.n - 2:
                break
            actions = []
            if j0 > j:
                if i0 == it:
                    actions.append(Direction.DOWN)

                actions.append(Direction.LEFT)
            else:
                actions.append(Direction.RIGHT)
            animate_plan(puzzle, actions)
            i0, j0 = puzzle.tile_pos[0]
            i, j = puzzle.tile_pos[target_tile]

    # Move the blank tile to the same position of the
    # target tile
    while i0 != i:
        if i0 > i:
            animate_plan(puzzle, [Direction.UP])
        else:
            animate_plan(puzzle, [Direction.DOWN])
        i0, j0 = puzzle.tile_pos[0]
    if j == puzzle.n - 1 and j0 == puzzle.n - 2:
        animate_plan(puzzle, [Direction.RIGHT])


def has_to_move_right(puzzle: NPuzzle, j: int, jt: int) -> bool:
    """
    We move to right if target position is on the right side
    of the j position
    """
    return j < jt or j == jt and jt == puzzle.n - 1


def move_left_down_row(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    This is used for the cases in which the target tile is
    on the last column. It assumes the blank tile will be
    on the left
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.DOWN,
        Direction.LEFT,
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


def move_target_tile_to_row_left(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    We move the target tile to the left side of board.
    If we find the target tile column, then we move up otherwise
    we move diagonally to the left.
    """
    i0, j0 = puzzle.tile_pos[0]
    i, j = puzzle.tile_pos[target]
    while (i, j) != (it, jt):
        if j == jt:
            move_up_left(puzzle, target, it, jt, left_limit, up_limit)
        elif i == it:
            move_left_down_row(puzzle, target, it, jt, left_limit, up_limit)
        else:
            move_diagonally_left(puzzle, target, it, jt, left_limit, up_limit)
        i, j = puzzle.tile_pos[target]


def move_right_down(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Moves a tile to the right, passing the blank tile down the target
    tile.
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.LEFT,
        Direction.DOWN,
        Direction.RIGHT,
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


def move_target_tile_to_row_right(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    In the case the target position is to the right of the current target
    tile position, we call this function. This function moves the target
    from (i, j) to (it, jt) using "right" moves.
    """
    i0, j0 = puzzle.tile_pos[0]
    i, j = puzzle.tile_pos[target]
    while (i, j) != (it, jt):
        # Cases in which the target tile is on the last column
        if j == puzzle.n - 1 and j0 == j - 1:
            move_up_right(puzzle, target, it, jt, left_limit, up_limit)
        # We found the target column position. We need to move up
        elif j == jt:
            move_up_left(puzzle, target, it, jt, left_limit, up_limit)
        # This is a corner case when the tile is already in the target row
        # But not in place. We need to be careful of not moving tiles on
        # the left of this tile so we move right passing the blank down the tile
        elif i == it:
            move_right_down(puzzle, target, it, jt, left_limit, up_limit)
            i, j = puzzle.tile_pos[target]
            i0, j0 = puzzle.tile_pos[0]
            # This is for the case in which we move the second to last tile
            # To close the row we need to be below the last moved tile
            if j0 == j - 1:
                animate_plan(puzzle, [Direction.DOWN, Direction.RIGHT])
        else:
            if i0 - 1 != up_limit or (jt - 1 == j and it != up_limit):
                move_diagonally_right(puzzle, target, it, jt, left_limit, up_limit)
                i, j = puzzle.tile_pos[target]
                if jt == j == puzzle.n - 1 and it != i:
                    animate_plan(puzzle, [Direction.LEFT, Direction.UP])
            else:
                move_right_down(puzzle, target, it, jt, left_limit, up_limit)
                if jt == puzzle.n - 1 == j:
                    animate_plan(puzzle, [Direction.LEFT, Direction.UP])

        i, j = puzzle.tile_pos[target]
        i0, j0 = puzzle.tile_pos[0]


def complete_row(puzzle: NPuzzle) -> None:
    """
    Completes the row. When we are finishing a row, we move
    the second to last tile to the position (1, n) and the last
    tile to the position (2, n). For example in a 4x4 board we
    would have the following state:

    -----------------
    |  1|  2| 12|  3|
    -----------------
    | 14| 13|  8|  4|
    -----------------
    | 10|  6| 15|   |
    -----------------
    |  7| 11|  9|  5|
    -----------------

    This function applies the actions needed to get to:

    -----------------
    |  1|  2|  3|  4|
    -----------------
    | 14| 13| 12|   |
    -----------------
    | 10|  6|  8| 15|
    -----------------
    |  7| 11|  9|  5|
    -----------------
    """
    plan = [
        Direction.LEFT,
        Direction.UP,
        Direction.UP,
        Direction.RIGHT,
        Direction.DOWN,
    ]
    for action in plan:
        animate_plan(puzzle, [action])


def move_blank_to_target_down(
    puzzle: NPuzzle, target_tile: int, it: int, jt: int
) -> None:
    """
    This follows a similar logic, but puts the blank tile below
    the target tile. Mostly used to move tiles to the target column.
    We also use it to address some corner cases when we are completing
    rows.
    """
    # Corner case in which the target position is at the end
    # and the target tile is as well at the end
    # In this case the blank will be on the above the target
    i0, j0 = puzzle.tile_pos[0]
    i, j = puzzle.tile_pos[target_tile]
    if it == puzzle.n - 1 and i == puzzle.n - 1:
        if i0 == i:
            action = Direction.UP
            animate_plan(puzzle, [action])
        else:
            while i0 != i - 1:
                action = Direction.DOWN
                animate_plan(puzzle, [action])
                i0, j0 = puzzle.tile_pos[0]
    else:
        # In any other case we just move the blank
        # below the target
        limit = i + 1 if i < puzzle.n - 1 else i - 1
        while i0 != limit:
            if i0 > i:
                action = Direction.UP
            else:
                action = Direction.DOWN
            animate_plan(puzzle, [action])
            i0, j0 = puzzle.tile_pos[0]
            i, j = puzzle.tile_pos[target_tile]
            limit = i + 1 if i < puzzle.n - 1 else i - 1
            # We don't want to get stuck in case that the
            # tile is at the bottom
            if i == puzzle.n - 1 and i0 == puzzle.n - 2:
                break

    # Move the blank tile to the same position of the
    # target tile
    while j0 != j:
        if j0 > j:
            animate_plan(puzzle, [Direction.LEFT])
        else:
            animate_plan(puzzle, [Direction.RIGHT])
        i0, j0 = puzzle.tile_pos[0]
    if i0 < i and not (it == puzzle.n - 1 and i == puzzle.n - 1):
        animate_plan(puzzle, [Direction.DOWN])
        i0, j0 = puzzle.tile_pos[0]
        i, j = puzzle.tile_pos[target_tile]

    # We always will want to be below the target tile
    if i == puzzle.n - 1 and i0 == puzzle.n - 2 and it != puzzle.n - 1:
        animate_plan(puzzle, [Direction.DOWN])


def prevent_disturbing_row(puzzle, tile, i, j):
    """
    This fix cases in which we want to place a target tile and
    the tile target + 1 is already in place. We move the target + 1
    out of its position to avoid disturbing it while moving target
    """
    pos = puzzle.tile_pos[tile]
    # Case in which the last tile is already in its position
    # We need to take it out of it so we can move the previous
    # tile to position N without disturbing the row
    if pos == (i, j):
        move_blank_to_target_down(puzzle, tile, i, j)
        animate_plan(
            puzzle,
            [
                Direction.UP,
                Direction.LEFT,
                Direction.DOWN,
                Direction.DOWN,
                Direction.RIGHT,
                Direction.UP,
            ],
        )


def process_row(puzzle: NPuzzle, it: int, start_value: int) -> None:
    """Complete a row.

    In this context, by completing a row we mean that we get all the
    tiles in the target row sorted.

    For example if our starting puzzle is:

    -----------------
    | 15| 14| 13| 12|
    -----------------
    | 11| 10|  9|  8|
    -----------------
    |  7|  6|  5|  4|
    -----------------
    |  3|  1|  2|   |
    -----------------

    After calling this method the puzzle will look like:

    -----------------
    |  1|  2|  3|  4|
    -----------------
    | 14| 13| 12|   |
    -----------------
    | 10|  6|  8| 15|
    -----------------
    |  7| 11|  9|  5|
    -----------------
    """
    target_tile: int = start_value
    left_limit, right_limit = it, it
    for jt in range(it, puzzle.n):
        i, j = puzzle.tile_pos[target_tile]
        if target_tile == puzzle.n * (it + 1) - 1:
            jt = puzzle.n - 1
            last = puzzle.n * (it + 1)
            prevent_disturbing_row(puzzle, last, it, jt)
        elif target_tile == puzzle.n * (it + 1):
            it = it + 1
        else:
            if target_tile + 1 in puzzle.tile_pos:
                (ii, jj) = puzzle.tile_pos[target_tile + 1]
                if (ii, jj) == (it, jt + 1):
                    prevent_disturbing_row(puzzle, target_tile + 1, it, jt + 1)
        move_blank_to_target(puzzle, target_tile, it, jt)
        # Target position is on the left side
        if has_to_move_right(puzzle, j, jt):
            move_target_tile_to_row_right(
                puzzle, target_tile, it, jt, left_limit, right_limit
            )
        else:
            move_target_tile_to_row_left(
                puzzle, target_tile, it, jt, left_limit, right_limit
            )
        target_tile += 1
    complete_row(puzzle)


def move_diagonally_down(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Moves the target tile diagonally up left. It assumes that the
    blank tile is down the target tile
    """
    plan = [
        Direction.UP,
        Direction.LEFT,
        Direction.DOWN,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.LEFT,
    ]

    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, up_limit, left_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break


def move_left_up(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Used for the cases in which the target is in the last row.
    Assumes that the blank is on top of the target
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.LEFT,
        Direction.DOWN,
        Direction.RIGHT,
        Direction.UP,
        Direction.LEFT,
    ]
    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, up_limit, left_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break


def move_diagonally_up(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Moves the target tile diagonally up. It assumes that the
    blank tile is on the down of the target tile
    """
    i0, j0 = puzzle.tile_pos[0]
    plan = [
        Direction.LEFT,
        Direction.UP,
        Direction.RIGHT,
        Direction.UP,
        Direction.LEFT,
        Direction.DOWN,
    ]

    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, up_limit, left_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        i0, j0 = puzzle.tile_pos[0]
        if (i, j) == (it, jt):
            break


def move_left_down(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    This moves the target tile to the left rotating down the tile
    to avoid touching the upper row (might be the already sorted one).
    Assumes the blank is down the target
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.LEFT,
        Direction.UP,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.LEFT,
    ]
    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, up_limit, left_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break


def has_to_move_down(puzzle: NPuzzle, i: int, it: int):
    """
    We move up if target position is on the above
    of the i
    """
    return i < it or i == it and it == puzzle.n - 1


def move_up_by_right(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
) -> None:
    """
    Assumes blank is below the target and that the target it is already
    placed in the target column
    """
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.RIGHT,
        Direction.UP,
        Direction.UP,
        Direction.LEFT,
        Direction.DOWN,
    ]
    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, up_limit, left_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break


def move_target_tile_to_column_up(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
):
    i0, j0 = puzzle.tile_pos[0]
    i, j = puzzle.tile_pos[target]
    while (i, j) != (it, jt):
        if i == it:
            move_left_down(puzzle, target, it, jt, up_limit, left_limit)
        elif j == jt:
            move_up_by_right(puzzle, target, it, jt, up_limit, left_limit)
        else:
            move_diagonally_up(puzzle, target, it, jt, up_limit, left_limit)
        i, j = puzzle.tile_pos[target]
    i0, j0 = puzzle.tile_pos[0]

    # For cases in which we move up the tile and end stuck in the
    # Target column
    if j0 == left_limit:
        animate_plan(puzzle, [Direction.RIGHT])
        if i0 > up_limit:
            animate_plan(puzzle, [Direction.UP])


def move_down(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
):
    i, j = puzzle.tile_pos[target]
    plan = [
        Direction.UP,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.DOWN,
        Direction.LEFT,
    ]
    for action in plan:
        i0, j0 = puzzle.tile_pos[0]
        if invalid_action(puzzle, i0, j0, action, up_limit, left_limit):
            break
        animate_plan(puzzle, [action])
        i, j = puzzle.tile_pos[target]
        if (i, j) == (it, jt):
            break


def move_target_tile_to_column_down(
    puzzle: NPuzzle, target: int, it: int, jt: int, left_limit: int, up_limit: int
):
    i0, j0 = puzzle.tile_pos[0]
    i, j = puzzle.tile_pos[target]
    while (i, j) != (it, jt):
        if i == puzzle.n - 1 == it:
            move_left_up(puzzle, target, it, jt, up_limit, left_limit)
        elif i == it:
            move_left_down(puzzle, target, it, jt, up_limit, left_limit)
        elif j == jt or (j == jt + 1 and it > i + 1):
            move_down(puzzle, target, it, jt, up_limit, left_limit)
            # Case in which I moved the target tile just one step down
            # and the goal is puzzle.n - 1
            i, j = puzzle.tile_pos[target]
            if i == puzzle.n - 1:
                animate_plan(puzzle, [Direction.RIGHT, Direction.DOWN])
        else:
            move_diagonally_down(puzzle, target, it, jt, up_limit, left_limit)
            i, j = puzzle.tile_pos[target]
            # If it is at the end of the row but it is not the last tile
            # to move
            if it == i == puzzle.n - 1:
                animate_plan(puzzle, [Direction.UP, Direction.LEFT])
        i, j = puzzle.tile_pos[target]
        i0, j0 = puzzle.tile_pos[0]

    # Case in which we moved diagonally down the second to last
    # tile to the last row
    if it == puzzle.n - 1 == i0 + 1:
        animate_plan(puzzle, [Direction.RIGHT, Direction.DOWN])


def complete_column(puzzle: NPuzzle):
    plan = [
        Direction.UP,
        Direction.LEFT,
        Direction.LEFT,
        Direction.DOWN,
        Direction.RIGHT,
    ]
    for action in plan:
        animate_plan(puzzle, [action])


def process_column(puzzle: NPuzzle, jt: int, start_value: int):
    target_tile = start_value + puzzle.n
    up_limit, left_limit = jt, jt
    for it in range(jt + 1, puzzle.n):
        i, j = puzzle.tile_pos[target_tile]
        if target_tile == 1 + puzzle.n * (puzzle.n - 1) + jt:
            jt = jt + 1
        elif target_tile == 1 + puzzle.n * (puzzle.n - 2) + jt:
            it = puzzle.n - 1

        move_blank_to_target_down(puzzle, target_tile, it, jt)
        # Target position is on the bottom side
        if has_to_move_down(puzzle, i, it):
            move_target_tile_to_column_down(
                puzzle, target_tile, it, jt, up_limit, left_limit
            )
        else:
            move_target_tile_to_column_up(
                puzzle, target_tile, it, jt, up_limit, left_limit
            )
        target_tile += puzzle.n
    complete_column(puzzle)
