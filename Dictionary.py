"""
Created by JamesW
This file was created with the purpose of learning the basics of Python programing
"""


"""Dictionaries can store almost limitless amount of information.
Understanding dictionaries allows you to model a variety of real-world
objects more accurately.
"""

enemy = {"color": "blue", "hp":  "4"}
print(enemy["color"])
print(enemy["hp"])

"""A key-value pair is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key. Every key
is connected to its value by a colon, and individual key-value pairs are separated by commas.
"""

"""Adding New Key-Value Pairs
Dictionaries are dynamic structures, and you can add new key-value pairs
to a dictionary at any time. For example, to add a new key-value pair, you
would give the name of the dictionary followed by the new key in square
brackets along with the new value."""

enemy["ammo"] = "laser"
print(enemy) #An additional key:value pair was added to the dictionary.


"""Starting with an Empty Dictionary
It’s sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it. 
To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value
pair on its own line."""

enemies = {} #Started with an empty list
enemies["powerup"] = "laser"
enemies["speed"] = 5 #Added two key:value pairs
print(enemies)
