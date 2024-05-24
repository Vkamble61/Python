# Create an Empty record_list
record_list =[]
# Create a list
record_list = ["Michael Jackson", 10.1, 1982,"MJ",1]
print(record_list)

# Indexing - we can use Positive and Negative Indexing
print("First item:",record_list[0])
print("Last item:",record_list[-1])

# Sample List can contain strings, floats, integers, nest other lists,  nest tuples and other data structures. 
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

# List slicing
print(record_list[2:4])#[1982, 'MJ']

# Use extend to add elements to list
record_list = [ "Michael Jackson", 10.2]
record_list.extend(['pop', 10]) # extend adds new elements to the list
print(record_list) #['Michael Jackson', 10.2, 'pop', 10]

# Use append to add elements to list

record_list = [ "Michael Jackson", 10.2]
record_list.append(['pop', 10]) #append adds one element to the list --> nested List
print(record_list) #['Michael Jackson', 10.2, ['pop', 10]]

#As lists are mutable, we can change them. Change the first element
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space. Convert a string to a list using split
print('hard rock'.split())
# Split the string by comma
print('A,B,C,D'.split(','))

#Copy and Clone List
A = ["hard rock", 10, 1.2]
B = A #A and B are referencing the same list in memory
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0]) #B[0]: hard rock
A[0] = "banana"
print('A[0]:', A[0]) #A[0]: banana
print('B[0]:', B[0]) #B[0]: banana

# Clone (clone by value) the list A
B = A[:]
print('A:', A)
print('B:', B)

# Examine the copy by value
print('B[0]:', B[0])
A[0] = "hard rock"
print('A[0]:', A[0]) #A[0]: hard rock
print('B[0]:', B[0]) #B[0]: banana