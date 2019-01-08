import random

random_list_one = random.sample(range(1, 20), 12)
random_list_two = random.sample(range(1, 20), 14)

common_list = [num for num in random_list_one if num in random_list_two]
print(set(common_list))
