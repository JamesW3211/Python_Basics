"""
Created by JamesW
This file was created with the purpose of learning the basics of Python programing
"""

#Datatypes - Strings

""" The first data type we’ll look at is the string.A string is simply a series of characters. 
Anything inside quotes is considered a string in Python, and you can use single or double quotes 
around your strings.
"""

string = "This is a string with double quotes"
string2 = 'This is a string with single quotes'
print(string)
print(string2)



#Reassigning the Value Inside Variables Using Strings

dessert = "Chocolate"
dessert = dessert + " Cake" #The value in the variable dessert was reassigned creating a new value.
print(dessert)

dessert = "Chocolate"
dessert += " Cake" #The above can be shortend using "In-place addition".
print(dessert)



#Title Method
"""
In this example, the lowercase string "jurassic park" is stored in the variable book_name. 
The method title() appears after the variable in the print() statement.
A method is an action that Python can perform on a piece of data. 
The dot (.) after name in name.title() tells Python to make the title() method act on the variable name. 
Every method is followed by a set of parentheses, since methods often need additional information to work.
That information is provided inside the parentheses. 
The title() function does not need any additional information, so its parentheses are empty.
title() displays each word in titlecase, where each word begins with a capital letter. 
This is useful because you’ll often want to think of a name as a piece of information. 
For example, you might want your program to recognize the input values Ada, ADA, and ada as the 
same name, and display all of them as Ada.
"""

book_name = "jurassic park"
print(book_name.title())


#Upper and Lower Method
"""The lower() method is particularly useful for storing data. Many times
you won’t want to trust the capitalization that your users provide, so you’ll
convert strings to lowercase before storing them. Then when you want to
display the information, you’ll use the case that makes the most sense for
each string."""


name = "joe anderson"
print(name.upper()) #The Upper method turns a string to all uppercase letters.

name = "Sally Liverpool"
print(name.lower()) #The Lower method turns a string to all lowercase letters.


#Concatenating Strings

"""Python uses the plus symbol (+) to combine strings. In this example,
we use + to create a full name by combining a first_name, a space, and a
last_name."""

first_name = "Joe"
last_name = "Boston"
full_name = first_name + " " + last_name

print(full_name)
print("Hello " + full_name.title())

#Adding Whitespace to Strings with Tabs or Newlines
"""In programming, whitespace refers to any non-printing character, such as
spaces, tabs, and end-of-line symbols. You can use whitespace to organize
your output so it’s easier for users to read."""


print("\tPython") # \t inserts whitespace equivalent to pressing tab

print("I am learning:\nPython\nJavascript") #To add a newline in a string, use the character combination \n.
print("I am learning:\n\tPython\n\tJavascript") #You can combine tabs and newlines in a single string.


#Stripping WhiteSpace
"""Python can look for extra whitespace on the right and left sides of a
string. To ensure that no whitespace exists at the right end of a string, use
the rstrip() method."""

car ="Porsche "
print(car) #When car is printed the first time, as space to the right of the variable's value is printed.
car.rstrip()
print(car) #When car is printed the second time, the space to the right of the variable's value is removed.
           #However, it is only removed temporarily.

"""To remove the whitespace from the string permanently, you have to
store the stripped value back into the variable:"""

car ="Porsche "
car = car.rstrip()
print(car) #Now the car variable has removed the whitespace permanently.


"""You can also strip whitespace from the left side of a string using the
lstrip() method or strip whitespace from both sides at once using strip():
"""

car = " Mercedes "
car = car.lstrip() #The whitespace only on the left side of the string is removed.
print(car)

car = " Mercedes "
car = car.strip() #The whitespace on both sides of the string is removed.
print(car)




