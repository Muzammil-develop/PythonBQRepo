# Python Scope:
    # A variable is only available from inside the region it is created is called Scope 
    
# Local Scope:
    # A variable created inside a function belongs to the local scope of that function 
# and can only be use inside that function

# def my_func():
#     x = 5
#     print(x)

# my_func()    

# FUNCTION INSIDE FUNCTION :
    # As explained in the example above , the variable x is not avilable outside the function , but it 
# is availabe for any function inside that function .

# def my_func():
#     x = 5

#     def nest_func():
#         print(x)
#     nest_func()

# my_func()

# GLOBAL SCOPE :
    # A variable created in the main body of the python code is a global variable and belongs to the 
# global scope 
    # Global variables are available from within any scope global and local

# x = 300

# def my_func():
#     print(x)

# my_func()

# print(x)

# NAMING VARIABLES :
    # If we operate with the same variables inside and outside of the function , Python will treat
# them as two separate variables , one available in the global scope (available outside the function) and
# one availabe in the local scope (inside the function)

# x = 300

# def my_func():
#     x = 200
#     print(x)

# my_func()

# print(x)

# GLOBAL KEYWORD:
    # If we need to create a global variable but are stuck in the local scope , we can use the global
# keyword . The global keyword makes the variable global 

# def my_func():
#     global x
#     x = 200
#     print(x)

# my_func()

# print(x)
    
    # Also use global keyword , if we want to make change to a global variable inside a function

# x = 300

# def my_func():
#     global x 

#     x = 200
#     print(x)

# my_func()

# print(x)

# NON LOCAL KEYWORD :
    # The non locaL keyword is used to work with variables inside nested function
    # The non local keyword makes the variable belongs to the outer function.

# def my_func():
#     x = 300

#     def inner_func():
#         nonlocal x 
#         x = 'Hello'

#     inner_func()
#     return x

# # my_func()
# print(my_func())









