name = "Michael Jackson"
print(name)

# Indexing
print(name[0]) # Print the first element in the string

# Negative Indexing
print(name[-1]) # Print the last element in the string

# Find the length of string
len("Michael Jackson")

# Slicing
print(name[0:4]) #Mich  # Take the slice on variable name with only index 0 to index 3 
print(name[8:12]) #Jack

#Stride

print(name[::2]) #McalJcsn # Get every second element. The elments on index 1, 3, 5 ...
print(name[0:5:2]) #Mca  # Get every second element in the range from index 0 to index 4

# Concatenation
print( name + " is the best") # Concatenate two strings

# Replicate strings
print(3 * name) # Print the string for 3 times

# Escape Sequence
print("Michael Jackson \n is the best" ) # New line escape sequence
print("Michael Jackson \t is the best" ) # Tab escape sequence
print("Michael Jackson \\ is the best" ) # Include back slash in string
print(r"Michael Jackson \ is the best" ) # r will tell python that string will be display as raw string

#String Manipulation Operations
print(name.upper()) # UPPERCASE
print(name.lower()) # lowercase

# Replace the old substring with the new target substring is the segment has been found in the string
print(name.replace('Michael', 'Janet'))

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
print(name.find('el')) #5
print(name.find('Jack')) #8
# If the sub-string is not in the string then the output is a negative one.
print(name.find('Jasdfasdasdf')) #-1

#Split the substring into list
print(name.split())

#String interpolation 
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

x = 10
y = 20
print(f"The sum of x and y is {x+y}.")