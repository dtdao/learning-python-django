# Make a game boad

def draw_game_box(val):
	print(" ---- "*int(val))
	print(" |  | "*int(val))
	print(" ---- "*int(val))
	return False

def draw_game_board():
	while True:
		try:
			size = int(input("What size game would you like? >>>>> "))
			break;
		except:
			print("That is not a number, try again")

	for x in range(0,size):
		draw_game_box(size)
	return

if __name__ == '__main__':
	draw_game_board()