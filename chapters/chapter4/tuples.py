# Defining a tuple
dimensions = (200, 50)
print("First dimension:", dimensions[0])
print("Second dimension:", dimensions[1])

# Attempting to change a tuple value (will cause an error if uncommented)
# dimensions[0] = 250  # TypeError: 'tuple' object does not support item assignment

# Looping through all values in a tuple
print("Looping through dimensions:")
for dimension in dimensions:
    print(dimension)

# Writing over a tuple (reassigning the variable)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Tuple with one element
single_element_tuple = (3,)
print("\nTuple with one element:", single_element_tuple)