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
print(cars[3]) #Lexus will be displayed.


"""You can also use the string methods on any element in a list."""
print(cars[2].title()) #Mercedes will be displayed in titlecase.

"""Index Positions Start at 0, Not 1
Python considers the first item in a list to be at position 0, not position 1.
This is true of most programming languages, and the reason has to do with
how the list operations are implemented at a lower level. """

"""Python has a special syntax for accessing the last element in a list. 
By asking for the item at index -1, Python always returns the last item in the list:"""

baseball_teams = ["Yankees", "Blue Jays", "Orioles", "Dodgers"]
print(baseball_teams[-1]) #The last item in the list is displayed.

"""You can use individual values from a list just as you would any other variable."""
print("My favorite baseball team is the " + baseball_teams[0].title()) #String concatenation + Method


"""Changing, Adding, and Removing Elements"""

"""To change an element, use the name of the list followed
by the index of the element you want to change, and then provide the new
value you want that item to have."""

colors = ["red", "yellow", "blue", "orange", "purple"]
print(colors)

colors[0] = "white"
print(colors) #The value in index 1 changed to white


"""Adding Elements to a List"""
"Python provides several ways to add new data to existing lists."

"""The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list without affecting any of the other elements in the list:"""



number_list = ["one","two", "three", "four"]
number_list.append("five")
print(number_list)


"""The append() method makes it easy to build lists dynamically. For
example, you can start with an empty list and then add items to the list
using a series of append() statements."""

vehicles = []
vehicles.append("Car")
vehicles.append("Truck")
print(vehicles)


"""Inserting Elements into a List
You can add a new element at any position in your list by using the insert()
method. """

books = ["Book 1", "Book 2", "Book 4"]
books.insert(2, "Books 3") #Book 3 was inserted into the list at index 2.
print(books)

"""Removing Elements from a List
You can remove an item according to its position in the list or according to its value. 
If you know the position of the item you want to remove from a list, you can use the del statement. 
"""

countries = ["usa", "germany", "china", "denmark"]
print(countries)
del countries[3]
print(countries) #denmark was deleted from the list

"""Removing an Item Using the pop() Method
Sometimes you’ll want to use the value of an item after you remove it from a
list. For example, you might want to get the x and y position of an alien that
was just shot down, so you can draw an explosion at that position."""

"""The pop() method removes the last item in a list, but it lets you work
with that item after removing it. """

letters = ["a", "b", "c", "d"]
print(letters)
letters.pop() #The last letter was removed from the list
print(letters)

"""If you know an items index, you can pop any items from a list."""

letters.pop(2)
print(letters) #C was removed from the list.

""""If you’re unsure whether to use the del statement or the pop() method,
here’s a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method."""

"""Removing an Item by Value
If you only know the value of the item you want to remove, you
can use the remove() method.
Note. The remove() method deletes only the first occurrence of the value you specify. 
If there’s a possibility the value appears more than once in the list, you’ll need to 
use a loop to determine if all occurrences of the value have been removed."""


flowers = ["sunflowers", "roses", "marigolds"]
print(flowers)
flowers.remove("roses")
print(flowers)



"""Organizing a List
Sorting a List Permanently with the sort() Method"""

writing_instruments = ["pen", "pencil", "marker"]
writing_instruments.sort()
print(writing_instruments) #The list is PERMANENTLY sorted alphabetically.

"""You can also sort this list in reverse alphabetical order by passing the
argument reverse=True to the sort() method."""

writing_instruments.sort(reverse=True)
print(writing_instruments) #The list is sorted in reverse alphabetical order.

"""Sorting a List Temporarily with the sorted() Function
to maintain the original order of a list but present it in a sorted order, you
can use the sorted() function."""

random_things = ["shoe","car","sky", "water"]
print("Here is the original list: ")
print(random_things)

print("\nHere is the sorted list:")
print(sorted(random_things))

print("\nHere is the original list again: ")
print(random_things) #The sorted list was only temporary

"""Printing a List in Reverse Order
To reverse the original order of a list, you can use the reverse() method. """

electronics = ["cell phone","laptop", "camera"]
print(electronics)
electronics.reverse()
print(electronics)


""""Finding the Length of a List
You can quickly find the length of a list by using the len() function."""

print(len(electronics))
