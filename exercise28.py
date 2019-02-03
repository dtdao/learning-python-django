def max_of_three(var1, var2, var3):
	if var1 > var2 and var1 > var3:
		return print(var1)
	elif var2 >  var1 and var2 > var3:
		return print(var2)
	else:
		return print(var3)

if __name__ == '__main__':
	max_of_three(4,100,8)