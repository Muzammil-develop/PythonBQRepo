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

# KEYWORD ARGUMENTS :
    # We can also send arguments with key= value syntax
    # This way the order of argument does not matter . 

# def name(child1,child2,child3):
#     print('The youngest child is ' + child3)

# name(child1='John' , child2='Larry' , child3='Khan') 

    # The phrase keyword argument are often shortened to kwargs in Python documentation .

# ARBITARY KEYWORD ARGUMENT (**kwargs):
    # If you donot know how many keyword arguments that will be passed into function , add two 
# asterik  : ** before parameter name in the definition . 
    # This way the function can recieve a dictionary of arguments and can access the items accordingly

# def name(**kwargs):
#     for i in kwargs.values():
#         print('Child name is ' + i)

# name(child1 = 'john' , child2 = 'larry')

# NOTE :    
    # Arbitary keyword argument are often shortened to **kwargs in python documentation

# DEFAULT PARAMETER VALUE :
    # The followig example shows how to use a default parameter value
    # If we call the function without arguments ,it uses the default value

# def country(default="Pakistan"):
#     print('My country name is ' + default)

# country('Bahrain')
# country()

# PASSING A LIST AS AN ARGUMENT :
    # We can send any datatypes of arguments to a function (string , lit , number , dictionary etc)
# and it will be treated as he same data type inside the function .
    # If we send list as an arguments , it will still be a list when it reaches a function 

# def food(fruits):
#     for fruit in fruits:
#         print(fruit)

# fruits = ['apple' , 'banana' , 'mango']

# food(fruits)

# RETURN VALUES :
    # To let a function return values , use return statement .

# def multiply(x):
#     return 5 * x

# print(multiply(2))
# print(multiply(5))

# PASS STATEMENT :
    # function definition can not be empty , but for some rason if we want function with no content
# then we have to use 'pass' keyword in order to not get error 

# def func():
    # pass 

# POSITIONAL ONLY ARGUMENTS :   
    # We can specify that a function can only have a positional arguments or ONLY keyword arguments
    # To specify that function can only have positional arguments add ',/' after arguments.
    
# def my_func(x , /):
#     print(x)

# my_func(5)  

    # Without ,/ we are actually allowed to use keyword arguments evewn if the function can expects 
# positional arguments . 

# def my_func(x):
#     print(x)

# my_func(x = 5)

    # but when we added ',/'we will get an error if we try to send a keyword argument

# def my_func(x , /):
#     print(x)

# my_func(x=5)

# KEYWORD ONLY ARGUMENT:
    # To specify that a function ca only have keyword arguments add '*,' before the arguments

# def my_func(* , x):
#     print(x)

# my_func(x = 5)

    # Without the '*,' we are allowed to use positional arguments if the function expects keyword 
# arguments .

# def my_func(x):
#     print(x)

# my_func(5)  

    # But with '*,' we will get an error if we try to send a positional arguments

# def my_func(* , x):
#     print(x)

# my_func(5)

# COMBINE POSITIONAL ONLY AND KEYWORD ONLY :
    # We can combine the two arguments type in the same function.

    # Any arguments before the '/ ,' are positional only and any arguments after '*,'  are keyword
# only

# def my_func(a , b , /, *, c , d):
#     print(a + b + c + d)

# my_func(5 , 6 , c = 10 , d = 20)  

# RECURSION :
    # Python also accepts function recursion , which means a defined function can all itself.
    
    # Recursion is a common mathematical and programming concept . It means that a function can call
# itself . This has the benefit of meaning that we can loop through a data to reach a result

    # The developer should be very careful with recursion as it can be quite easy to slip into writing a 
# function which never terminates or one that uses excess amount of memory or processor power . However
# when written correctly recursion can be very efficient and mathematically-elegent approach to 
# programming 

    # In this example tri_recursion() is a function to we have defined to call itself (resurse) . we use
# the k variable as the data . which decrements (-1) every time we recurse  . The recursion ends when the 
# condition is not greater than 0 (when it is 0).

    # To  a new developer it can take some time to work out how exactly this works , best way to find out
# this is by testing or modifying it .

# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
    
# print('Recursion Example Results :' )

# tri_recursion(6)











