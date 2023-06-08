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

