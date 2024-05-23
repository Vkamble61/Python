#RegEx (short for Regular Expression) is a tool for matching and handling strings.
#This RegEx module provides several functions for working with regular expressions, including search, split, findall, and sub.
#Python provides a built-in module called re, which allows you to work with regular expressions

# search() used to search for the word "Jackson" in the string "Michael Jackson is the best".
import re
sent = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, sent)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

#Special Sequence	Meaning	            Example
#\d	Matches any digit character (0-9)	"123" matches "\d\d\d"
#\D	Matches any non-digit character	"hello" matches "\D\D\D\D\D"
#\w	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
#\W	Matches any non-word character	"@#$%" matches "\W\W\W\W"
#\s	Matches any whitespace character (space, tab, newline, etc.)	"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
#\S	Matches any non-whitespace character	"hello_world" matches "\S\S\S\S\S\S\S\S\S"
#\b	Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
#\B	Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

#The findall() finds all occurrences of a specified pattern within a string.
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text) 
print("Matches:", matches) #Matches: [',', ' ', '!']


# Use the findall() function to find all occurrences of the "as" in the string
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
print(re.findall("as", s2)) #['as', 'as']


# Use the split function to split the string by the "\s"
print(re.split("\s", s2)) #['Michael', 'Jackson', 'was', 'a', 'singer', 'and', 'known', 'as', 'the', "'King", 'of', "Pop'"]


# Define the regular expression pattern to search for
pattern = r"King of Pop"
# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
print(re.sub(pattern, replacement, s2, flags=re.IGNORECASE)) #Michael Jackson was a singer and known as the 'legend'

