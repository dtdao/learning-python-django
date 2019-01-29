import random


def let_me_guess():
	guess = random.randint(0, 100)
	low = 0
	high = 100
	guess_count = 1
	while True:
		while True:
			try:
				answer = input(f"My guess is {guess}? Is it 'correct'? Or is it 'too high' or 'too low'? ")
				answer = answer.lower()
				assert(answer in ['too high', 'too low', 'correct', 'exit'])
				break
			except:
				print("invalid answer")

		if answer == 'too high':
			high = guess-1
			guess = random.randint(low, high)
			guess_count += 1
		elif answer == 'too low':
			low = guess+1
			guess = random.randint(low, high)
			guess_count += 1
		elif answer == 'correct':
			print(f"Hooray I did it!!, it took me {guess_count} tries before I got your correct number")
			break
		else:
			print("Game Finished")
			break

if __name__ == '__main__':
	let_me_guess()