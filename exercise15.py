testing_string = "This is the story of my life and how I made it all the way over'here!"

def reverse_string(string):
	holder = string.split(" ")[::-1]
	return print("<<<< " + " ".join(holder))

reverse_string(input("""Please enter a string for me to reverse for you >>>>> 
 >>>>  """))

