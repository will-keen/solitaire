""" Classes to represent the solitaire game board"""

BOARD_WIDTH = 7
MIN_VAL = 2
MAX_VAL = BOARD_WIDTH - 2

def index_is_legal(x, y):
	return (((x >= MIN_VAL and x < MAX_VAL) and ((y >= MIN_VAL) or (y < MAX_VAL))) or
			((y >= MIN_VAL and y < MAX_VAL) and ((x >= MIN_VAL) or (x < MAX_VAL))))

class Space:
	""" Represents one space on the game board"""

	def __init__(self, legal, occupied):
		""" Create a space - either it can
			accept a piece or not"""
		self.legal = legal
		self.occupied = occupied

	def as_string(self):
		""" Returns string representation of space"""
		space_str = " " if not self.legal else "o" if self.occupied else "."
		return space_str

class Board:
	""" Represents the game board, containing the spaces"""

	def __init__(self):
		""" Create the basic game board"""
		self.spaces = [[None for x in range(BOARD_WIDTH)] for y in range(BOARD_WIDTH)]
		for x in range(BOARD_WIDTH):
			for y in range(BOARD_WIDTH):
				is_legal = index_is_legal(x,y)
				self.spaces[x][y] = Space(is_legal, True)
		self.spaces[3][3].occupied = False

	def move_legal(self, x, y, dir):
		""" For a given space, returns true if there is a
			legal move in that direction"""
		if not (self.spaces[x][y] and self.spaces[x][y].legal and self.spaces[x][y].occupied):
			return False
		if dir == "right":


	def get_moves(self):
		""" Returns all currently legal moves, as a list of
		    boards that represent legal next states"""
		# Find sequences of occupied spaces followed by an
		# occupied and an unoccupied space in the same axis
		for x in range(BOARD_WIDTH):
			for y in range(BOARD_WIDTH):
				current = self.spaces[x][y]
				if (current.occuped):
					if (self.spaces[x+1][y] and self.spaces[x+1][y])

	def as_string(self):
		""" Returns a string denoting the game board"""
		board_str = ""
		for x in range(BOARD_WIDTH):
			for y in range(BOARD_WIDTH):
				board_str += self.spaces[x][y].as_string()
			board_str += "\n"
		return board_str[:-1]
