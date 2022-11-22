"""
Created by JamesW
This file was created with the purpose of learning the basics of Python programing
"""


"""
A list is a collection of items in a particular order. You can put anything you want into a list, 
and the items don’t have to be related in any particular way. 
It’s a good idea to make the name of your list plural, such as letters, digits, or names.
In Python, square brackets ([]) indicate a list, and individual elements
in the list are separated by commas.
"""

cars = ["honda", "toyota", "mercedes", "lexus", "jeep"]
print(cars)

"""Accessing Elements in a List
Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired."""

cars = ["honda", "toyota", "mercedes", "lexus", "jeep"]
print(cars[3])

print(cars[2].title())

"""Index Positions Start at 0, Not 1
Python considers the first item in a list to be at position 0, not position 1.
This is true of most programming languages, and the reason has to do with
how the list operations are implemented at a lower level. """



""" For Loop(For in Loop)
For each element
In a sequence
Loop do this action
"""


baseball_teams = ["Yankees", "Blue Jays", "Orioles"]
print(baseball_teams)

for each_element in baseball_teams:
    print(each_element)

"""This line tells Python to retrieve the first value from the list of baseball
teams and store it in the variable each_element. """



for x in range(1,5):
    print(x)

number = list(range(1,5))
print(number)
