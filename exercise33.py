import datetime 

def birthday_look():
	birthday_dict = {
	"John Smith": datetime.date(1906, 5, 31),
	"Jane Doe": datetime.date(1997, 6, 9),
	"Steve Coons": datetime.date(1988, 3, 20)
	}
	print(f"**** Welcome to britday look up program, we know the name of: ****")
	for x in birthday_dict:
		print(x)

	who_to_look_up = input("Whose birthday would you like to look up? >>>> ")
	if who_to_look_up in birthday_dict:
		print(f"{who_to_look_up}'s' birthday is on {birthday_dict[who_to_look_up]}")
	else:
		print("Sorry that name is not in our directory")

if __name__ == '__main__':
	birthday_look()