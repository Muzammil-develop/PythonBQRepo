# FUNCTION:
    # A function is a block of code which only runs when it calls . 

    # We can pass data known as paramter into a function.

    # A function can return data as a result .

# CREATING A FUNCTION :
    # In Python a function is defined using def keyword

# def fun():
#     print('Hello Function')

# fun()

# CALLING A FUNCTION :
    # To call a function use function name followed by parenthesis 

# def fun():
#     print('Hello From function')

# fun()

# ARGUMENTS :
    # Information can be passes into functions are called arguments 

    # Argements are specified after function name inside parenthesis . We can add as many arguments as
# we want . just separate them with a comma . 

    # The following example has a function with 1 argument (fname) . when function is called , we pass
# along a first name which is used inside a function to print the full name .

# def name(fname):
#     print( fname + ' first name')

# name('john')

# NOTE :    
    # Arguments are often shorthand to args in python documentation .

# PARAMETERS OR ARGUMENTS : 
    # The term parameter and arguments can be used for the same thing , information that are passed into 
# a function .

# From a function prespective :

# 1. A parameter is the variable listed inside the paranthesis in the function definition . 
# 2. An argumnet is the value that is sent to the information when it is called .

# NUMBER OF ARGUMENTS :
    # by default a function can be called with correct number of arguments . Meaning that if our 
# function expects 2 arguments . we have to call the function with 2 arguments  , not more , not less

# def name (fname , lname):
#     print(fname + ' ' + lname)

# name('john' , 'larry') 

    # if we try to call function with 1 or 3 arguments we got an error like this :

# name('john')

# ARBITRARY ARGUMENTS (*args):
    # If we do not know how many arguments that will be passed into our function . and a * befor the 
# parameter name in the function definition . 
    
    # This way function recieved arguments in tuple and can access items accordingly

# def func(*childs):
#     for i in childs:
#         print("Child name is " + i)

# func('john' , 'harry' , 'khan')   

# NOTE :
    # Arbitary arguments are often shortened to *args in python documentation













