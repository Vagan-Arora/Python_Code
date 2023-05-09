""" Python variables are the reserved memory locations used to store values with in a Python Program. This means that
 when you create a variable you reserve some space in the memory.

In Python, a variable is a name to which a value is assigned. When you create a variable, you set it equal to a value
"""

x = 26
y = "vagan"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4     #x is of type int
x = 'sally'  # now x is now of type str
print(x)


#Casting
#If you want to specify the data type of a variable, this can be done with casting.

x = str (3)    # x will be '3'
y = int (3)    # y will be 3
z = float (3)  # z will be 3.0


#Get the Type
#You can get the data type of a variable with the type() function.

x = 14
y = 'vagan1'

print(type(x))
print(type(y))

#What is a Data Type?
'''
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:
By default, python provides the following built-in data types:

1. Numeric data: int, float, complex
int = 3, -8, 0

float= 7.349, -9.0, 0.0000001

complex: 6 + 2i
2. Text data: str
str=  "Hello World!!!", "Python Programming"

#3. Boolean data:
#Boolean data consists of values True or False.
4. Sequenced data: list, tuple

list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
'''


#Case-Sensitive

a = 15
A = "Vagan"

print(a)
print(A)
##A will not overwrite a

#There are several techniques you can use to make them more readable:

#Camel Case
myVariableName = "Dell"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"




#Assign Multiple Values

#Python allows you to assign values to multiple variables in one line:

x,y,z = "Orange","Banana","Cheery"
print(x,y,z)



#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = 5
z = "awesome"
print(x, y, z)


#Global Variables
"""
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

"""

#Exercises in python

#Exercises 1

# Create a variable called “name” and set it equal to your name.

Name = "Vagan Arora"
print(Name)

#Exercises 2
#Create a variable called “age” and set it equal to your age

age = 2
print(age)

#Exercises 3
#Create a variable called “favorite_number” and set it equal to your favorite number.

favorite_number = 29
print(favorite_number)

#Exercises 4
# Create a variable called “gpa” and set it equal to your current grade point average.

#Exercises 5
#Create a variable called “favorite_animal” and set it equal to your favorite animal.

favorite_animal   = "Alka"
print(favorite_animal)

#Create a variable called “favorite_color” and set it equal to your favorite color.
#Exercises 6
favorite_color  = "Black"


#Exercises 7
#Create a variable called “hobby” and set it equal to your favorite hobby.

Hobby = "Tech"
print(Hobby)


#Exercises 8
#Create a variable called “dream_job” and set it equal to your dream job.

dream_job = "In Hacking"
print(dream_job)
