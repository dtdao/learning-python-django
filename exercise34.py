import json
import datetime

# Simple function to add a new name to the database
def add_new_birthday():
	with open("birthday.json", "r") as f:
		info = json.load(f)

	name = input("What is the first and last name of the person you want to add? >>>>> ").strip()
	birthday = input(f"What is {name}'s birthday? (yyyy-mm-dd) >>>>> ").strip()

	info["people"].append({"name": name, "birthday": birthday})

	with open("birthday.json", "w") as f:
		json.dump(info, f)

	print(f"#########Congratulations you added {name} to the database.############\n")
	birthday_lookup()

# Main birthday lookup function
def birthday_lookup():
	with open("birthday.json", "r") as f:
		info = json.load(f)
	print("We currently know the birthdays of : >>>>> ")
	for x in info["people"]:
		print(x["name"])

	who_to_look_up = input("Whose birthday would you like to look up? >>>>> ")

	birthday = [x["birthday"] for x in info["people"] if x["name"] == who_to_look_up]

	if birthday:
		print(f"{who_to_look_up}'s birthday is on {birthday}")
	else:
		print("Sorry please check your name, or we might not have that in the system.")
		option = input("Would you like to add a new name or search for a different person? (new/search) >> ").lower()
		if option == "search":
			return birthday_lookup()
		else:
			return add_new_birthday()

if __name__ == '__main__':
	birthday_lookup()