import time
from enum import Enum
from typing import Dict, List, Tuple


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def generate_template_board(n, is_goal: bool = False):
    """Generate a board with the worst case given a dimension n.

    In this case we generate a board with the reversed ordering of
    the tiles. The only catch is that for the puzzle to be solvable
    the last two tiles should be swapped if n is even.

    For example, for n = 4, the board is:

    -----------------
    | 15| 14| 13| 12|
    -----------------
    | 11| 10|  9|  8|
    -----------------
    |  7|  6|  5|  4|
    -----------------
    |  3|  1|  2|   |
    -----------------

    Note that for n = 3 the last two tiles are not swapped:

    -------------
    |  8|  7|  6|
    -------------
    |  5|  4|  3|
    -------------
    |  2|  1|   |
    -------------

    If `is_goal` is True, the board is the goal state of the puzzle.
    """
    board = []
    curr = n * n - 1 if not is_goal else 1
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(curr)
            curr -= 1 if not is_goal else -1
        board.append(row)
    board[n - 1][n - 1] = 0

    # For the puzzle to be solvable in the case of
    # even number of tiles the last two tiles should
    # be swapped
    if n % 2 == 0 and not is_goal:
        board[n - 1][n - 2], board[n - 1][n - 3] = (
            board[n - 1][n - 3],
            board[n - 1][n - 2],
        )
    return board


class NPuzzle:
    def __init__(self, board: List[List[int]], is_goal: bool = False) -> None:
        # Simple assertions to make sure the board is "valid"
        assert len(board) > 0
        assert len(board[0]) > 0
        assert len(board) == len(board[0])
        assert all(len(row) == len(board[0]) for row in board)

        self.board = board
        n = len(board)
        self.n = n
        self.tile_pos: Dict[int, Tuple[int, int]] = {}
        for i in range(n):
            for j in range(n):
                self.tile_pos[board[i][j]] = (i, j)

    def move(self, dir: Direction) -> bool:
        """Move the blank tile given a direction

        In the case of a valid move, the blank tile is moved
        to the new position, and the tile at the new position
        is moved to the old position. If the move is invalid,
        the board is unchanged and this method returns False.
        """
        (zero_i, zero_j) = self.tile_pos[0]
        if dir == Direction.UP:
            i, j = zero_i - 1, zero_j
        elif dir == Direction.DOWN:
            i, j = zero_i + 1, zero_j
        elif dir == Direction.LEFT:
            i, j = zero_i, zero_j - 1
        else:
            i, j = zero_i, zero_j + 1
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return False
        tile = self.board[i][j]
        self.tile_pos[0] = (i, j)
        self.tile_pos[tile] = (zero_i, zero_j)
        self.board[i][j], self.board[zero_i][zero_j] = (
            self.board[zero_i][zero_j],
            self.board[i][j],
        )
        return True

    def __str__(self) -> str:
        """String representation of the board"""
        s = ""
        line = "----" * self.n + "-\n"
        s += line
        for row in self.board:
            s += "|"
            for col in row:
                if col:
                    s += f"{col: >3}" + "|"
                else:
                    s += f"{' ': >3}" + "|"
            s += "\n" + line

        return s

    def __repr__(self) -> str:
        """String representation of the board"""
        return str(self)

    def __hash__(self) -> int:
        """Hash function for the board"""
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        """Equality function for the board"""
        if not isinstance(other, NPuzzle):
            raise NotImplementedError("Other object must be an NPuzzle object")
        return all(row1 == row2 for row1, row2 in zip(self.board, other.board))


def draw_puzzle(puzzle) -> None:
    s = ""
    line = "----" * puzzle.n + "-\n"
    s += line
    for row in puzzle.board:
        s += "|"
        for col in row:
            if col:
                i, j = puzzle.tile_pos[col]
                array_index = i * puzzle.n + j
                if col == array_index + 1:
                    col_str = f"{bcolors.OKGREEN}{col: >3}{bcolors.ENDC}"
                else:
                    col_str = f"{col: >3}"
                s += col_str + "|"
            else:
                s += f"{' ': >3}" + "|"
        s += "\n" + line
    print(s)


def clear_output():
    print("\033c", end="")


def animate_plan(puzzle, plan):
    clear_output()
    draw_puzzle(puzzle)
    for action in plan:
        clear_output()
        time.sleep(0.2)
        puzzle.move(action)
        draw_puzzle(puzzle)
