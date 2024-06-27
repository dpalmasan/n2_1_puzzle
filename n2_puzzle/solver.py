from typing import List, Optional

from n2_puzzle.puzzle import Direction, NPuzzle


class State:
    def __init__(
        self,
        puzzle: NPuzzle,
        action: Optional[Direction] = None,
        parent: Optional["State"] = None,
        depth: int = 0,
    ):
        self.puzzle = puzzle
        self.action = action
        self.parent = parent
        self.depth = depth

    def neighbors(self) -> List["State"]:
        neighbors = []
        for dir in Direction:
            board = [list(row) for row in self.puzzle.board]
            new_puzzle = NPuzzle(board)
            if new_puzzle.move(dir):
                neighbors.append(State(new_puzzle, dir, self, self.depth + 1))
        return neighbors

    def __repr__(self) -> str:
        return repr(self.puzzle)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, State):
            raise NotImplementedError("Other object must be a State object")
        return self.puzzle == other.puzzle

    def __hash__(self) -> int:
        return hash(self.puzzle)
