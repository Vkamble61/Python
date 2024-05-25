"""Functions"""
# if.. elif.. else
def check_age():
    """Check age"""
    age = 15

    if age > 2 and age < 12:
        print("Under 12 not allowed")
   # elif age > 12 or age < 17:
   #     print("Teenager Allowed with one adult")
    #elif not(AGE >= 17):
    #    print("Not allowed")
    elif age > 18:
        print("You are allowed" )
    elif age == 18:
        print("Go see Pink Floyd")
    else:
        print("Go see Meat Loaf" )

    print("Rock on")
    #return(None)

check_age()

######### For Loop
#for i in range(-3, 3): #prints out all the element between -2 and 3
#    print(i)

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for item in squares:
    print(item)

for i in range(0, 5):
    print("Square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value
for i, square in enumerate(squares):
    print(i, square)

######## While Loop
dates = [1982, 1980, 1973, 2000]
i = 0
YEAR = dates[0]
while YEAR != 1973:
    print(YEAR)
    i += 1
    YEAR = dates[i]
print("It took ", i ,"repetitions to get out of loop.")

## Print time table
#for i in range(6,8):
#    for j in range(1,11):
#        print(i * j)

# To count the words in the sentence
SENTENCE = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb. \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

def freq(sent):
    """Calculate Frequency of words"""
    words = []
    words = sent.split()
    dict1 = {}
    for key in words:
        dict1[key] = words.count(key)
    print("The frequency of word is: ",dict1)

freq(SENTENCE)

# Example for setting param with default value

def is_good_rating(rating=4):
    """If condition"""
    if rating < 7:
        print("this album sucks it's rating is",rating)
    else:
        print("this album is good its rating is",rating)
is_good_rating()
is_good_rating(10)

# Example of global variable

ARTIST = "Michael Jackson"
def printer_one(artist):
    """SCOPE of variable"""
    internal_var1 = artist
    print(ARTIST, "is an artist")
    print(internal_var1, "is an artist")

printer_one(ARTIST)
# try runningthe following code
#printer1(internal_var1)  ## the variable assignment does not persist outside the function.

ARTIST = "Michael Jackson"

def printer(artist):
    """Global variable"""

    #global internal_var

    internal_var= "Whitney Houston"
    print(artist,"is an artist")
    print(internal_var,"is an artist")

printer(ARTIST)
#printer(internal_var)

# When the number of arguments are unknown for a function, They can all be packed into a tuple
def print_all(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    """Multiple args"""
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
#printAll with 3 arguments
print_all('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
print_all('Sidecar','Long Island','Mudslide','Carriage')

#Similarly, The arguments can also be packed into a dictionary as shown:
def print_dictionary(**args):
    """Dictionary args"""
    for key in args:
        print(key + " : " + args[key])
print_dictionary(Country='Canada',Province='Ontario',City='Toronto')

#Functions can accept (and return) data types, objects and even other functions as arguements.
def add_items(list1):
    """Append"""
    list1.append("Three")
    list1.append("Four")

myList = ["One","Two"]

add_items(myList)

print(myList)
