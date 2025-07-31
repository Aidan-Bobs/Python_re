# 4-1. Pizzas
pizzas = ["pepperoni", "margherita", "hawaiian"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!\n")

# 4-2. Animals
animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!\n")

# 4-3. Counting to Twenty
for number in range(1, 21):
    print(number)
print()

# 4-4. One Million
# Uncomment the next lines to print all numbers from 1 to 1,000,000
# for number in range(1, 1000001):
#     print(number)

# 4-5. Summing a Million
million_numbers = list(range(1, 1000001))
print("Min:", min(million_numbers))
print("Max:", max(million_numbers))
print("Sum:", sum(million_numbers))
print()

# 4-6. Odd Numbers
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
print()

# 4-7. Threes
threes = list(range(3, 31, 3))
for number in threes:
    print(number)
print()

# 4-8. Cubes
for number in range(1, 11):
    print(number ** 3)
print()

# 4-9. Cube Comprehension
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)
print()

# 4-10. Slices
print("The first three items in the list are:", cubes[:3])
print("Three items from the middle of the list are:", cubes[3:6])
print("The last three items in the list are:", cubes[-3:])
print()

# 4-11. My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append("veggie")
friend_pizzas.append("bbq chicken")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print()

# 4-12. More Loops
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)