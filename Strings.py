name = "Michael Jackson"
print(name)
# Indexing
# Print the first element in the string
print(name[0])
# Negative Indexing
# Print the last element in the string
print(name[-1])
# Find the length of string
len("Michael Jackson")
# Slicing
# Take the slice on variable name with only index 0 to index 3
print(name[0:4]) #Mich
print(name[8:12]) #Jack
#Stride
# Get every second element. The elments on index 1, 3, 5 ...
print(name[::2]) #McalJcsn
# Get every second element in the range from index 0 to index 4
print(name[0:5:2]) #Mca
# Concatenation
# Concatenate two strings
print( name + " is the best")
# Replicate strings
# Print the string for 3 times
print(3 * name)
# Escape Sequence
# New line escape sequence
print("Michael Jackson \n is the best" )
# Tab escape sequence
print("Michael Jackson \t is the best" )
# Include back slash in string
print("Michael Jackson \\ is the best" )
# r will tell python that string will be display as raw string
print(r"Michael Jackson \ is the best" )
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