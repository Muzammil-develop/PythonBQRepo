# Introduction

# Python is a high level programming language which is developed by Guido Van Rossum in 1991 . Python is
# used in web-development , app-development , data-science , AI , ML etc . It is a esay language which
# can be learn by Anyone . Working with python is  like working in English . Due to this feature . 
# Beginners love this languaga


# Variable :
    # A variable is a container to store some values or datatypes . Perhaps there is some rules for 
    # creating variables . These are 

# 1 . Variables can not start with numbers
# 2 . A variable name can contain alphanumerice number (A-Z , 0-9 , _)
# 3 . Variable name are case sensitive means "avg" and "Avg" are separate Variables 

# Note :
    # In the world of Programming and Development . We always gives those name to varaibles which can 
# make sense or align with the work we done . so tht it help others to understand what we are doing
# in it .   

# value = 1
# print(value)

# Comments :
    # Suppose we want to document our code . but when we write document and run it with code . It throw 
    # error here comments come . We use it to document our code without getting Error . There are 2
    # types of comment

# 1 . Single Line Comment (#)

# This is comment 
# a = 10  

# 2 . Multiline Comment (''')

'''
This is
Multi line
comment
'''

# Variables types can be changed once they are assigned

# x = 4
# x = 'String'
# print(x)

# Type-casting :
    # if we want to change variable type from one to another we use casting

# a = 3
# a = str(a)
# print(a)

# Type:
    # if we want to know type of variables we use type function to fing what type of values store in
    # this variable

# a = 'Ahmed'
# print(type(a))

# String Variables :
    # String variables can be defined by using single quote string , or double quote string

# a = 'ahmed'
# print(a)

# b = "ahmed"
# print(b)

# Multi Words Variable Name 
    # variables name with more than one word are difficult to read . There are several techniques to
    # write this name 

    # 1 . Camel Case
        # Each word except First word start with Capital letter Like this:

# myVariableName = 'John'

    # 2 . Pascal Case:
        # Each word starts with a capital letter

# MyVariableName = 'John'

    # 3 . Snake Case :
        # Each word is separated by a '_' like this:

# my_variable_name = 'John' 

# Assign Multiple values to Multiple variables :
    # We can assign multiple values to multiple variables in 1 line . Make sure the number of
    # variables is same as number of values otherwise it throw an error .

# x,y,z = 'Apple','Orange','Banana'
# print(x)
# print(y)
# print(z)

# One values to Multiple Variables :  
    # We can assign one values to multiple variables like this :

# x = y= z = 'Orange'
# print(x)
# print(y)
# print(z)

# Unpack Collection :
    # If we have an collection of values stored in a list or tuple . We can unpack its values using
    # variables like this :

# collection = ['Fan' , 'Table' , 'Chair']
# x,y,z = collection
# print(x) 
# print(y) 
# print(z) 

# Output variables :
    # In python print() function is the output variables . It is used to print values from variables

# x = 'Kite'
# print(x)

    # we can also print multiple values from variables in a print function by separating , like this:

# a = 'Apple'
# b = 'Banana'
# c = 'Chair'

# print(a,b,c)

    # we can also use + operator to output multiple variables . But remember we have to provide space
    # after storing each variable otherwise it will result in combination of variables without space

# a = 'Apple'
# b = 'Banana'
# c = 'Chair'

# print(a + b + c)

# like this :

# a = 'Apple '
# b = 'Banana '
# c = 'Chair'

# print(a + b + c)

# Note:   
    # If we use + operator in a variables containing numbers it will perform mathematical operation

# a = 10
# b = 5
# print(a + b)

    # If we try to combine string and number using  + operator . It will result in Error

# a = 10
# b = 'John'
# print(a + b)

# Best Way :
    # The best way to output multiple variables is using , in print function . so it will return all
    # values from it whether of different datatype

# a = 10
# b = 'banana'
# print(a , b)



