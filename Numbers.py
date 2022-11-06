"""
Created by JamesW
This file was created with the purpose of learning the basics of Python programing
"""
from math import*  #imports math functions
import random



#Working with Numbers


"""There are three numeric types in Python:
1.int
2.float
3.complex

1.Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
2.Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
3.Complex numbers are written with a "j" as the imaginary part:
"""
x = 5    # int
y = 2.8  # float
z = 1j   # complex

"""Number type Conversion:
You can convert one number type to another using the int(), float(), and complex() methods:
"""
a = 5    # int
b = 2.8  # float
c = 1j   # complex


a = float(a) #conversion from int to float:
b = int(b) #conversion from float to int:
c = complex(c) #conversion from int to complex:

print(a)
print(b)
print(c)

print(type(a)) #To verify the type of any object in Python, use the type() function:
print(type(b)) #To verify the type of any object in Python, use the type() function:
print(type(c)) #To verify the type of any object in Python, use the type() function:


#Displaying Numbers
print(9) #Simple way to display a whole number
print(2.563) #You can print integers
print(-2.0987) #You can print negative numbers
print(1j) #You can print complex numbers


#Numbers and Math Operations
"""
You can add (+), subtract (-), multiply (*), and divide (/) integers in Python. 
"""
print(3 + 4.5) #Addition is possible
print(3 - 4.5) #Subtration is possible
print(3 * 4.5) #Multiplication is possible
print(3 / 4.5) #Division is possible

print(3 * 4 + 5) #Multiple mathematical operations are possible in one function
print(3 * (4 + 5)) #Order of operations is possible
print(10 % 3) #Modulus function provides the remainder

my_num = -5
print(abs(my_num)) #Absolute value of a number

my_num = -5
print(pow(3, 2)) #Raising a number to a power

my_num = -5
print(sqrt(36)) #Finds the square root of a number


#Numbers and Strings

"""
If you want to use numbers inside of strings, you have to convert a number into a string
using the str() method. 
"""

my_num = 5
print(my_num) # You can store numbers into variables

my_num = 5
print(str(my_num)) # You can convert numbers into a string

my_num = 5
print(str(my_num) + " is my favorite number") #Converts a number into a string then concatenates two strings together.


#Numbers and Set Operations

my_num = -5
print(max(4, 6)) #Find the largest number from a set of numbers

my_num = -5
print(min(4, 6)) #Finding the lowest number from a set of numbers

my_num = -5
print(round(3.7)) #Round a number

my_num = -5
print(floor(3.7)) #Finding the lowest number from a set of numbers

my_num = -5
print(floor(3.7)) #Round the integer down to a whole number

my_num = -5
print(ceil(3.7)) #Rounds the integer up to a whole number


#Random Numbers

print(random.randrange(1, 10)) #Prints a random number between 1 and 9. Python index starts at 0.  

