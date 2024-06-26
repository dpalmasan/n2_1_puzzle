from typing import List, Dict, Tuple

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

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
        self.board[zero_i][zero_j], self.board[i][j])
        return True

    def __str__(self) -> str:
        """String representation of the board"""
        s = ""
        line = "----"*self.n +  "-\n"
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

    def __eq__(self, other: "NPuzzle") -> bool:
        """Equality function for the board"""
        for row1, row2 in zip(self.board, other.board):
            if row1 != row2:
                return False
        return True
