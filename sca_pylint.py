# Static code analysis is an application code efficiency verification activity that analyses source
# code for #quality, reliability and security without executing the code. Static code analysis is an
# essential part of any application development cycle.
# One of the most popular frameworks is PyLint, which evaluates the code against compliance with the
# PEP8 coding style guide and generates comments wherever it finds an issue.
# https://uk.mathworks.com/discovery/static-code-analysis.html
# https://en.wikipedia.org/wiki/Static_program_analysis
# https://peps.python.org/pep-0008/

# Install pylint from Marketplace it will automatically analyze the code. Check it on Problem window
# OR pip3 install pylint==2.11.1
# Run pylint sample1.py in terminal

# Python Enhancement Proposal 8 (PEP8), is a coding style guide for Python Programming.
# It is a widely recognized style guide for writing high-quality code.

#  Following two code snippet for static code analysis
#Your code has been rated at -1.67/10
""" def add(number1,number2):
    return number1+number2
num1 = 4
num2 = 5
total = add(num1, num2)
print("The sum of {} and {} is {}".format(num1,num2,total))

 """
# Issues with above code are
# Exactly one space required after comma
# Exactly one space required around assignment
# Constants should be Uppercase

#sample.py modified using Pylint
#Your code has been rated at 10.00/10

def add(number1, number2):
    """Add Two numbers"""
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
