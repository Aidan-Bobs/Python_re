# Exercise 6-1: Person Information
print("=== Exercise 6-1: Person Information ===")
person = {
    'first_name': 'Sarah',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'Seattle'
}

print(f"First Name: {person['first_name']}")
print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

print("\n" + "="*50 + "\n")

# Exercise 6-2: Favorite Numbers
print("=== Exercise 6-2: Favorite Numbers ===")
favorite_numbers = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 13,
    'Diana': 25,
    'Edward': 3
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

print("\n" + "="*50 + "\n")

# Exercise 6-3: Glossary
print("=== Exercise 6-3: Programming Glossary ===")
glossary = {
    'variable': 'A named storage location that holds a value which can be changed during program execution.',
    'function': 'A reusable block of code that performs a specific task and can accept parameters and return values.',
    'loop': 'A programming construct that repeats a block of code multiple times based on a condition.',
    'list': 'An ordered collection of items that can be changed, allowing duplicate values and different data types.',
    'dictionary': 'A collection of key-value pairs where each key is unique and maps to a specific value.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:")
    print(f"    {meaning}\n")

# Exercise 6-4: Glossary 2 (Expanded with 5 more terms)
print("=== Exercise 6-4: Expanded Programming Glossary ===")
glossary_expanded = {
    'variable': 'A named storage location that holds a value which can be changed during program execution.',
    'function': 'A reusable block of code that performs a specific task and can accept parameters and return values.',
    'loop': 'A programming construct that repeats a block of code multiple times based on a condition.',
    'list': 'An ordered collection of items that can be changed, allowing duplicate values and different data types.',
    'dictionary': 'A collection of key-value pairs where each key is unique and maps to a specific value.',
    'string': 'A sequence of characters used to represent text data in programming.',
    'integer': 'A whole number data type that can be positive, negative, or zero.',
    'boolean': 'A data type that can only have two values: True or False.',
    'tuple': 'An ordered collection of items that cannot be changed after creation.',
    'module': 'A file containing Python code that can be imported and used in other programs.'
}

# Using a loop instead of individual print statements
for word, meaning in glossary_expanded.items():
    print(f"{word.title()}:")
    print(f"    {meaning}\n")

print("="*50 + "\n")

# Exercise 6-5: Rivers
print("=== Exercise 6-5: Rivers ===")
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

# Print sentences about each river
print("Rivers and their countries:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers in the dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries in the dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")

print("\n" + "="*50 + "\n")

# Exercise 6-6: Polling
print("=== Exercise 6-6: Polling ===")
# Simulating the favorite_languages dictionary from the book
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# List of people who should take the poll
poll_list = ['alice', 'jen', 'bob', 'sarah', 'charlie', 'edward', 'diana']

print("Polling Results:")
for person in poll_list:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"Hi {person.title()}, please take our favorite languages poll!")