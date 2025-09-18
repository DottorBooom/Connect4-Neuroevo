from random import randint
import numpy as np

X = 1  # Player X
Y = -1  # Player Y

def printBoard(board):
	''' This function prints the board in a human-readable format.
		X is represented by 1, O by -1 and empty cells by 0.

		Input:
			board: the game board (numpy 2D array)

		Output:
			None (prints the board to the console)
	'''

	RED = '\033[31m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	RESET = '\033[0m'

	for r in range(board.shape[0]):
		row = board.T[r]
		s = []
		for v in row:
			if v == 1:
				s.append(f"{BLUE}| {RED}X{BLUE} |{RESET}")
			elif v == -1:
				s.append(f"{BLUE}| {YELLOW}O{BLUE} |{RESET}")
			else:
				# dot and borders in blue
				s.append(f"{BLUE}| {BLUE}.{BLUE} |{RESET}")
		print("".join(s))

	for c in range(board.shape[1]):
		# print column indices with blue borders
		print(f"{BLUE}| {c} |{RESET}", end="")
	print("\n")  # empty line to separate turns

	return None

def insertMove(move, value, board, availableMoves) -> bool:
	''' This function inserts the moves of player X and player Y into the board.
		After the insertion, if the row is full (no more 0), it removes the row from availableMoves.
		The function use the rows as "columns" of the game. So x and y are row indices.
		This method allow a good use of the locality of reference (cache friendly).
		
		In the board, the player X is represented by 1 and player Y by -1.

		Input: 
			move: the row index where to insert the move (0-7)
			value: 1 for player X, -1 for player Y
			board: the game board (numpy 2D array)
			availableMoves: list of row indices that still have at least one 0 (empty cell)

		Output:
			Return False if a player cannot move because the row is full, True otherwise.
	'''
	def _drop_in_row(row_idx, value):
		''' Find the last index with 0 in the row row_idx and set it to 
			And, if this was the last zero in the row, remove the row from availableMoves.

			Input:
				row_idx: index of the row in the board
				value: value to insert (1 for player X, -1 for player Y)
			
			Output:
				Return False if the row is full (no 0 found), True otherwise.
		
			Example:
			row = [0, 0, 0, -1, 1]
			The last index with 0 is 2, so set row[2] = value
			row becomes [0, 0, 1, -1, 1] and because row is a reference to board[row_idx], 
			the board is updated as well.
		'''
		row = board[row_idx]
		zeros = np.where(row == 0)[0]
		if zeros.size == 0:
			return False
		last_zero_idx = zeros[-1]
		board[row_idx, last_zero_idx] = value

		if zeros.size == 1:
			# If this was the last zero in the row, remove the row from availableMoves
			availableMoves.remove(row_idx)
		return True

	# Insert for x (1)
	if not _drop_in_row(move, value):
		print(f"Row {move} is full for player {value}")
		return False # Early return if a player cannot move
	
	return True 

def checkWin(board, x, value) -> bool:
	''' This function checks if there is a winner in the game.
		It checks all rows, columns and diagonals (close to last_move) for a sequence of 4 identical non-zero values.

		Input:
			board: the game board (numpy 2D array)
			last_move: the last move made (row index)
			value: the player that is been checked

		Output:
			True if there is a winner, False otherwise.
	'''

	# First, let's find the (x,y) coordinate of the last move
	row = board[x]
	nonzeros = np.where(row != 0)[0]
	y = nonzeros[0]

	# Check vertical (column)
	if len(nonzeros) >= 4:
		if row[y] == row[y + 1] == row[y + 2] == row[y + 3] == value:
			return True
	
	# Check horizontal (row)
	start = max(0, x - 3)
	end = min(board.shape[0] - 1, x + 3)
	line = [board[c, y] for c in range(start, end + 1)]

	if len(line) >= 4:
		for i in range(0, len(line) - 3):
			if (line[i] == value and line[i+1] == value and line[i+2] == value and line[i+3] == value):
				return True

	# Check diagonal (top-left to bottom-right) and (top-right to bottom-left)
	# Build diagonal sequences centered at (x,y) using offsets -3..+3 and clip to board bounds.
	rows = board.shape[0]
	cols = board.shape[1]

	# Diagonal 1: top-left to bottom-right -> positions (x + i, y + i)
	diag1 = []
	for i in range(-3, 4):
		nx = x + i
		ny = y + i
		if 0 <= nx < rows and 0 <= ny < cols:
			diag1.append(board[nx, ny])

	if len(diag1) >= 4:
		for i in range(0, len(diag1) - 3):
			if diag1[i] == value and diag1[i+1] == value and diag1[i+2] == value and diag1[i+3] == value:
				return True

	# Diagonal 2: top-right to bottom-left -> positions (x + i, y - i)
	diag2 = []
	for i in range(-3, 4):
		nx = x + i
		ny = y - i
		if 0 <= nx < rows and 0 <= ny < cols:
			diag2.append(board[nx, ny])

	if len(diag2) >= 4:
		for i in range(0, len(diag2) - 3):
			if diag2[i] == value and diag2[i+1] == value and diag2[i+2] == value and diag2[i+3] == value:
				return True

	return False

def main():

	# Initialize all the available columns in the board (0-7). This will allow a random selection of moves
	availableMoves = [x for x in range(8)]

	# Initialize the board as an 8x8 numpy array. More faster than a list of lists
	board = np.zeros((8, 8))

	# Simulate a game
	while len(availableMoves) > 0:
		x_move = availableMoves[randint(0, len(availableMoves) - 1)]

		if not insertMove(x_move, X, board, availableMoves):
			print(f"Invalid move: ({x_move}, {y_move}) \n Board: {board}")
			return 1 # Exit if a player cannot move

		print(f"Player X: {x_move} rank")
		printBoard(board)
		if checkWin(board, x_move, X):
			print("Player X wins!")
			return 0

		y_move = availableMoves[randint(0, len(availableMoves) - 1)]

		if not insertMove(y_move, Y, board, availableMoves):
			print(f"Invalid move: ({x_move}, {y_move}) \n Board: {board}")
			return 1 # Exit if a player cannot move

		print(f"Move Y: {y_move} rank")
		printBoard(board)
		if checkWin(board, y_move, Y):
			print("Player Y wins!")
			return 0

	return 0

if __name__ == "__main__":
	if main() is not 0:
		print("Game ended with an error.")
