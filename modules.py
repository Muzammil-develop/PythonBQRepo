# PYTHON MODULE:
    # Consider a ppython module to be same as a code library
    # A file containing a set of functions we want to include in our application.

# CREATE A MODULE .
    # To create a module save the code you want in a file with the file extension called '.py'

# USE A MODULE:
    # Now we can use the module we just created by using the import statement

# import mymodule

# mymodule.greeting('John')

# NOTE:
    # When using the function from a module use a syntax: module_name,function_name

# VARIABLES IN MODULES:
    # The module can contain function , as already described , but also variables of
# all types (arrays, dictionares , objects etc)

# import mymodule

# a = mymodule.person1['age']
# print(a)

# NAMING A MODULE:
    # We can name the module file whatever we like but it must have a file extension called '.py'

# RENAMING MODULE:
    # We can create an alias when we import a module , by using as keyword .

# import mymodule as mx

# a = mx.person1['age']
# print(a)

# BUILT-IN MODULES:
    # There are several buil-in modules in Python , Which can import whenever we like 

# import platform

# x = platform.system()
# print(x)

# USING DIR FUNCTION :
    # There is a built-in function to list all the function names (or variables name) in a module .
# The dir() function.

# import platform

# x = dir(platform)
# print(x)

# NOTE:
    # The dir function can be used on all modues . also the ones we create for ourself

# IMPORT FROM MODULE :
    # We can choose to import only parts from a module by using the from keyword 

# from mymodule import person1

# print(person1['age'])

# NOTE :
    # When importing using from keyword , do not use module name when referring to elements in the
# module . Example person1['age'] , not mymodule.person1['age']





