from enum import Enum, auto


class GameStatus(Enum):
	ACTIVE = auto()
	BLACK_WIN = auto()
	WHITE_WIN = auto()
	CONCEDE = auto()
	ABANDON = auto()
	CHECK_INITIATED = auto()
	CHECK_MATE = auto()


FOUR_DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
EIGHT_DIRECTIONS = FOUR_DIRECTIONS + [[-1, -1], [1, 1], [-1, 1], [1, -1]]
ROWS = 8
COLUMNS = 8
