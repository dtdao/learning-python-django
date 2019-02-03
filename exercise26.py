
# This check the state of a 3x3 matrix board for a winner.
# matrix = [0[0,1,2],
#           1[0,1,2],
#           2[0,1,2]]

def checking_(state_array):
	if all(p == 1 for p in state_array):
		return 1
	elif all(x == 2 for x in state_array):
		return 2

# matrix[1][1] = 1
def tic_tac_board(board_matrix_list):
	# this currently checks for horizontal winners
	for val in range(3):
		winner = checking_(board_matrix_list[val])
		if winner == 1 or winner ==  2:
			return print(f"Player {winner} is the winner!")

	# This double for loop check the vertical
	for x in range(3):
		vertical_holder = []
		for y in range(3):
			vertical_holder.append(board_matrix_list[y][x])
		winner = checking_(vertical_holder)
		if winner == 1 or winner ==  2:
			return print(f"Player {winner} is the winner!")

	if board_matrix_list[1][1] == (board_matrix_list[0][0] and board_matrix_list[2][2]) or board_matrix_list[1][1] == (board_matrix_list[0][2] and board_matrix_list[2][0]):
		return print(f"Player {board_matrix_list[1][1]} is the winner!")
	# This loop checks for the 


	return print("There are no winners")

if __name__ == '__main__':
	game = [[1, 0, 1],[2, 1, 0],[1, 0, 2]]
	game2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
	game3 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]

	tic_tac_board(game)
	tic_tac_board(game2)
	tic_tac_board(game3)