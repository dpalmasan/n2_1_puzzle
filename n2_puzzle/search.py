from typing import List, Optional

from n2_puzzle.puzzle import Direction, NPuzzle
from n2_puzzle.utils import PriorityQueue


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


def manhattan_distance(s1: State, s2: State) -> int:
    """Manhattan distance heuristic.

    Given s1 and s2, return the Manhattan distance between them.
    In this case if i1, j1 are coordinates of s1 and i2, j2 are
    coordinates of s2, the manhattan distance is computed by
    `abs(i1 - i2) + abs(j1 - j2)`.
    """
    distance = 0
    for row in s1.puzzle.board:
        for tile in row:
            i1, j1 = s1.puzzle.tile_pos[tile]
            i2, j2 = s2.puzzle.tile_pos[tile]
            distance += abs(i1 - i2) + abs(j1 - j2)

    return distance


def a_star_puzzle(init_state, goal_state) -> List[Direction]:
    """A* search algorithm for the 8-puzzle problem.

    In theory it supports any size of the board,
    but in practice it only works for 3x3 boards. The reason
    being that the search space increases exponentially with the size
    of the board.
    """
    queue = PriorityQueue()
    queue.push(
        init_state, manhattan_distance(init_state, goal_state) + init_state.depth
    )
    visited = set()
    plan: List[Direction] = []
    while not queue.isEmpty():
        state = queue.pop()
        visited.add(state)
        if state == goal_state:
            while state:
                if state.action:
                    plan.insert(0, state.action)
                state = state.parent
            break
        for neighbor in state.neighbors():
            if neighbor not in visited:
                queue.push(
                    neighbor, manhattan_distance(neighbor, goal_state) + neighbor.depth
                )
    return plan
