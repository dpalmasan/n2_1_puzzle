# $N^2 - 1$ Sliding Puzzle Solver

The generalization of the classical fifteen puzzle (15-puzzle) or eigth sliding puzzle (8-puzzle). This repository implements an $N^2 - 1$ puzzle interface as well as a solver based on the paper [A Real-Time Algorithm for the $(N^2 − 1)-Puzzle$](https://ianparberry.com/pubs/saml.pdf).

The algorithm in simple terms, moves each row and column tiles 1 by 1 to their target locations, and does this iteratively, until we end up with a 3x3 grid. At this point we apply A* (A-star) algorithm and solve the rest of the puzzle.


To run:

1. Run `poetry install`
2. `poetry run python main.py --n 5`

![15-puzzle](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/02ce9febfa07ad7dcc4e801baa07722d781d6bb2/15-puzzle.gif)


Try with different values for `n`.


I just did this for fun 😊
