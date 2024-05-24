# A set is a unique collection of objects in Python. You can denote a set with a pair of {}. 
# Python will automatically remove duplicate items:

# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)

# Set Operations
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

# Add element to set
A.add("NSYNC")
print("Added element ", A)

# Remove the element from set
A.remove("NSYNC")
print("Removed element ", A)

# Verify if the element is in the set
print("AC/DC" in A)

# Sets Logic Operations

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
print("Album Set1 ",album_set1)
print("Album Set2", album_set2)

# Find the intersections

intersection = album_set1 & album_set2
print("Intersection is : ",intersection)

# Use intersection method to find the intersection of album_list1 and album_list2
print("Intersecion:",album_set1.intersection(album_set2))   

# Find the difference in set1 but not set2
print("Only Album1 elements: ",album_set1.difference(album_set2)) # all the elements that are only contained in album_set1 
print("Only Album2 elements: ",album_set2.difference(album_set1)) #The elements in album_set2 but not in album_set1

# Find the union of two sets
print("Union : ",album_set1.union(album_set2)) #The union corresponds to all the elements in both sets

# Check if superset
print(set(album_set1).issuperset(album_set2))
print(album_set1.issuperset({"Back in Black", "AC/DC"}) )

# Check if subset
print(set(album_set2).issubset(album_set1))  
print(set({"Back in Black", "AC/DC"}).issubset(album_set1) )

