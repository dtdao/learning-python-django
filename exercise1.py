import datetime

def age_in_100_years(age,name):
    year = int(datetime.datetime.now().year)

    year_of_one_hundred = ((100 - age) + year)
    
    print(f"Hello {name}, you will turn 100 in the year {year_of_one_hundred}.")
    

name = input("What is your name? ")
age = int(input("How old are you? "))

age_in_100_years(age, name)





