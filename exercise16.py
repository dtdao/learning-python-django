import random
import time
import string

pass_list = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family', 'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother', 'Mr', 'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question', 'right', 'room', 'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time', 'water', 'way', 'week', 'woman', 'word']
weak_list = ['123456', 'Password', '12345678', 'qwerty', '12345', '123456789','letmein', '1234567', 'football', 'iloveyou', 'admin', 'welcome', 'monkey', 'login', 'abc123', 'starwars', '123123', 'dragon', 'passw0rd', 'maste', 'hello', 'freedom', 'whatever', 'qazwsx']

def generate_password(level):
	if level.lower() == "weak":
		return print(''.join(random.choice(pass_list) for _ in range(2)))
	elif level.lower() == "medium":
		return print(''.join(random.choice(string.hexdigits) for _ in range(7)))
	elif level.lower() == "hard":
		return print(''.join(random.choice(string.hexdigits + pass_list[random.randrange(1, len(pass_list))]) for _ in range(15)))
	elif level.lower() == "super hard":
		return print(''.join(random.choice(string.hexdigits + string.punctuation) for _ in range(10000)))
	else:
		return print(random.choice(weak_list))


how_hard = input("""
	How hard do you want your password to be?

	> Weak
	> Medium
	> Hard
	> Super Hard

	>>> """)

start = time.time()
generate_password(how_hard)
end = time.time()

print(f"Total Runtime: {end - start}")
