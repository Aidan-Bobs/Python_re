# A Simple Example: Car names
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

# Conditional Tests: Checking for Equality
car = 'bmw'
print(car == 'bmw')  # True

car = 'audi'
print(car == 'bmw')  # False
print()

# Ignoring Case When Checking for Equality
car = 'Audi'
print(car == 'audi')  # False
print(car.lower() == 'audi')  # True
print(car)  # 'Audi'
print()

# Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
print()

# Numerical Comparisons
age = 18
print(age == 18)  # True

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
print()

age = 19
print(age < 21)   # True
print(age <= 21)  # True
print(age > 21)   # False
print(age >= 21)  # False
print()

# Checking Multiple Conditions: and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # False

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # True
print((age_0 >= 21) and (age_1 >= 21))  # True
print()

# Checking Multiple Conditions: or
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)  # True

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)  # False
print()

# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' in requested_toppings)  # False
print()

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
print()

# Boolean Expressions
game_active = True
can_edit = False
print("Game active:", game_active)
print("Can edit:", can_edit)