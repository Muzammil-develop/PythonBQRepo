# PYTHON CLASSES AND OBJECT :
    # Python is an object oriented programming .
    # Almost everything in python is object with its properties and methods
    # A class is like an object constructor , or a blueprintfor creating objects .

# CREATE CLASS :
    # To create a class use keyword class

# class Person :
    # x = 5

# CREATE OBJECT:
    # NOw we use class name Person To create object 

# class Person:
#     x = 5

# a = Person()
# print(a.x)

# THE __init__ FUNCTION :
    # The examples above are classes and objects in their simplest form , and are not really useful in
# real life applications .
    # To understand the meaning of classes we have to understand the built-in __init__() function.
    # All classes have a function called __init__ () which always executed when class is being initiated
    # Use the __init__() function to assign values to object properties , or other operation that are 
# necessary to do when object is being created .

# class Person:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p = Person('John' , 20)

# print(p.name)
# print(p.age)

# NOTE:
    # The __init__() function is called automatically everytime when the class is being used to create
# a new object .

# THE __str__ FUNCTION:
    # The __str__() function controls what should be returned when the class object is represented as a
# string
    # If the __str__() function is not set , the string representation of the object is returned

# class Person:

#     def __init__(self,name , age):
#         self.name = name
#         self.age = age

# p = Person('John' , 20)
# print(p)

    # The string representation of object with __str__ function .

# class Person:

#     def __init__(self,name , age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'{self.name} ({self.age})'

# p = Person('John' , 20)

# print(p)

# OBJECT METHODS :
    # Object can also contains methods , Methods in objects are function that belong to the object 

# class Person :

#     def __init__(self, name , age):
#         self.name =  name
#         self.age = age

#     def func(self):
#         print('Hello my name is ' + self.name)

# p = Person('John' , 20)
# print(p)
# p.func()

# NOTE:
    # The self parameter is the reference to the current instance of class , and is used to access 
# the variables that belong to the class 

# SELF PARAMETER :
    # The selfparameter is the refernce ofto the current instance of class , and is used to access
# the variables that belongs to the class .
    # It does not have to be named self, we can call it whatever we like , but it has to first parameter
# of the any function in the class

# class Person:

#     def __init__(mysillyobject,name,age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def func(abc):
#         print('Hello my name is ' + abc.name )

# p = Person('John' , 36)
# p.func()

# MODIFY OBJECT PROPERTIES :
    # We can modify the properties on object like this

# class Person:

#     def __init__(mysillyobject,name,age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def func(abc):
#         print('Hello my name is ' + abc.name )

# p = Person('John' , 36)
# p.func()
# p.age = 40

# print(p.age)

# DELETE OBJECT PROPERTIES:
    # We can delete object properties by using del keyword 

# class Person:

#     def __init__(mysillyobject,name,age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def func(abc):
#         print('Hello my name is ' + abc.name )

# p = Person('John' , 36)
# p.func()
# p.age = 40

# del p.age 

# print(p.age)

# DELETE OBJECT :
    # We can delete any object by using del keyword .

# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def func(abc):
#         print('Your Age is ' + abc.age)

# p = Person('John' , 25)

# del p
# print(p.age)

# PASS STATEMENT :
    # We can use pass statement if we want our class definition empty . If we can not use pass it throw
# an error .

# class Person:
#     pass




