#The type of an expression by using the built-in type() function.
# Type of 12 is int
print(type(12))
# Type of 2.14 is float
print(type(2.14))
#Type of "Hello, Python 101!" is str
print(type("Hello, Python 101!"))
# Converting from one object type to a different object type
# Convert 2 to a float
print(float(2))
# Casting 1.1 to integer will result in loss of information
print(int(1.1))
# Convert a string into an integer
print(int('1'))
# Convert a string into an integer with error -- (string that is not a perfect match for a number)
# print(int('1 or 2 people'))
# Convert the string "1.2" into a float
print(float('1.2'))
# Convert an integer to a string
str(1)
# Convert a float to a string
str(1.2)
#An object of type Boolean can take on one of two values: True or False
print(type(True))
# Convert True to int
print(int(True))
# Convert 1 to boolean
print(bool(1))
print(type(4/2)) #float
print(type(4//2)) # int, as the double slashes stand for integer division 
