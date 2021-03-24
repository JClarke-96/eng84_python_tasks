import datetime

# Asks user for their name, age, and if they've had their birthday
def user_info():
    user_info.name = input("What is your name?    ")
    user_info.age = int(input("What is your age?    "))
    user_info.birthday_yet = input("Have you had your birthday this year? Y/N    ")

# Uses information asked to calculate the year of their birth
def calc_birth_year(name, age, birthday_yet):
    current_year = datetime.datetime.now()
    calc_birth_year.birth_year = current_year.year - age
    if birthday_yet == "N":
        calc_birth_year.birth_year -= 1

# Calls functions to ask for info and calculate birth year while new_user = True
# Asks if there is another user after each result has been printed to end the loop
new_user = True
while new_user:
    user_info()
    calc_birth_year(user_info.name, user_info.age, user_info.birthday_yet)
    print(f"{user_info.name} is {user_info.age} years old and was born in {calc_birth_year.birth_year}")
    is_new_user = input("Is there another user? True/False    ")
    if is_new_user == "False":
        new_user = False