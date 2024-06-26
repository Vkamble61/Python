
""" Tuples"""
# Create your first tuple
tuple1 = ("disco",10,1.2 )
print(tuple1)

# Print the type of the tuple you created
type(tuple1)

#Indexing
# Print the variable on each index
print(tuple1[0])
print(tuple1[1])

# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))

#Use negative index to get the value of the last element
print(tuple1[-1])

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2) #('disco', 10, 1.2, 'hard rock', 10)

#Slicing
print(tuple2[0:3]) # Slice from index 0 to index 2

# Get the length of tuple
print(len(tuple2))

#Sorting
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)# Sort the tuple
print(RatingsSorted)

# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])

# Print the first element in the second nested tuples

print("First charcter of 2, 1 of Tuple: ", NestedT[2][1][0])
