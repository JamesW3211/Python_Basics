"""
Created by JamesW
This file was created with the purpose of learning the basics of Python programing
"""


"""Looping Through an Entire List.
Looping allows you to take the same action, or set of actions,with every item in a list.  
When you want to do the same action with every item in a list, you can use Python’s for loop. 
"""


""" For Loop(For in Loop)
For each element
In a sequence
Loop do this action
"""


baseball_teams = ["Yankees", "Blue Jays", "Orioles"]
for each_element in baseball_teams:
    print(each_element)

"""Explanation of Looping Example
1. Python retrieves the first value (Yankees) from the list of baseball
teams and stores it in the variable "each_element." 
2. Python prints "Yankees" to the display. 
3. Python retrieves he second item from the list and repeats the process 
until all items are looped through, stored, and displayed. 

"""

"""Doing More Work Within a for Loop
You can do just about anything with each item in a for loop. 
All lines of code will be executed inside the for loop,
as long as the line following the initial for loop statement is indented.
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


"""Making Numerical Lists

Lists are ideal for storing sets of numbers, and Python provides a number of tools 
to help you work efficiently with lists of numbers. """


"""Using the range() Function
Python’s range() function makes it easy to generate a series of numbers.
The range() function causes Python to start counting at the first
value you give it, and it stops when it reaches the second value you provide.
Because it stops at that second value, the output never contains the end
value"""

for x in range(1,5):
    print(x)

"""Using range() to Make a List of Numbers
If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers."""

numbers = list(range(1,5))
print(numbers)

"""We can also use the range() function to tell Python to skip numbers
in a given range"""

odd_numbers = list(range(1,10,2)) #Starts at 1, adds 2 repeatedly until it reaches or passes the end value.
print(odd_numbers)

"""You can create almost any set of numbers you want to using the range()
function. Here’s how you might put the first 10 square numbers into a list:"""

squares = []  #start with an empty list
for value in range(1,11): #loop through each value 1 to 10 and store it in the variable "value"
    square = value **2 #numbers 1 to 10 is raised to the power of 10 and stored in the variable "square"
    squares.append(square) #each result is appended to the list "squares"
print(squares)


"""Simple Statistics with a List of Numbers"""


"""Simple Statistics with a List of Numbers"""

"""A few Python functions are specific to lists of numbers. For example, you
can easily find the minimum, maximum, and sum of a list of numbers:"""

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

"""Working with Part of a List"""

"""You can also work with a specific group of items in a list, which Python calls
a slice.To make a slice, you specify the index of the first and last elements you
want to work with. As with the range() function, Python stops one item
before the second index you specify."""

players = ["tony", "bob", "sally", "jamal", "quinn"]
print(players[0:3])

"""If you omit the first index in a slice, Python automatically starts your
slice at the beginning of the list:"""

print(players[:4])

"""If you omit the second index in a slice, it includes every value in the list 
after the first index."""

print(players[2:])

"""Recall that a negative index returns an element a certain distance from the end of a list;
therefore, you can output any slice from the end of a list.This prints the names of the last
three players and would continue to work as the list of players changes in size."""

print(players[-3:])
