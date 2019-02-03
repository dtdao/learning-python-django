# This function actually moves makes the moves 
def do_move(board_state, string, move_counter):
	#Sets the symbols to be use on the board, using the move_counter  
	symbol = ("X" if move_counter % 2 == 1 else "O")
	# This strip and then split the moves into an array
	move = string.strip().split(",")
	try:
		assert(board_state[int(move[0])][int(move[1])] == 0) 
		board_state[int(move[0])][int(move[1])] = symbol
	except:
		print("*****************INVALID MOVE******************")
		return board, move_counter
	move_counter += 1
	return board_state, move_counter

# This is the main game.  Loads clean board.
def main_game():
	# This move counter is to just keep track of what symbols to use
	total_moves = 1
	# This is an empty board
	game_board = [[0,0,0],[0,0,0],[0,0,0]]
	# This loops run as long as there is less or equal to 9 moves to be made on the board.
	while total_moves <= 9:
		# User is able to input the move of 
		move = input("Where would you like to move?  Please input in the coordinates as so>>>> row,col ")
		game_board, total_moves = do_move(game_board, move, total_moves)
		# Prints out the board state for players to see.
		print(*game_board, sep='\n')

# takes in the current board state and coordinates and change then return the new board to be display
if __name__ == '__main__':
	main_game()