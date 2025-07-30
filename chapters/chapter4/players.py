players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Slices
print(players[0:3])        # First three players
print(players[1:4])        # Second, third, and fourth players
print(players[:4])         # First four players
print(players[2:])         # From third player to the end
print(players[-3:])        # Last three players

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list using a slice
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Copying a list without a slice (both variables refer to the same list)
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)