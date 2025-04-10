# Strings :
    # Strings in python are surrounded by single quotes , double quotes . 'hello' is same as  "Hello"
    # we can display string literal with print() function 

# print('Hello')

# Quotes Inside Quotes :
    # We can use quotes inside quotes in string as long as they are not matched with the quotes
    # surrounded the string

# print("It's Alright")
# print('My name is "Muzammil"')

# Assign String to Variable :
    # We can assign a string to a variables by defining varables name followed by '=' , then string

# a = 'Hello'
# print(a)

# Multiline String :
    # We can assign multiline string by using triple quotes . 

# a = '''This is 
#     a multi-line
#     string'''
# print(a)

# # or 
# a = """This is 
#     a multi-line
#     string"""
# print(a)

# Strings are Arrays :
    # like many other popular programming languages , strings in oython are arrays of bytes representing
    # unicode characters 
    #  How ever python does not have a charactr datatype . a simple character can be a stings with a length 
    # of 1
    # Square brackets can be used to access elements from string . But indexing starts from 0

# a = 'Hello World'
# print(a[1])

# Looping through string :
    # since string are array we can loop through the characters using for loop

# for char in 'banana':
#     print(char)

# String Length:
    # We can get the length of string using len() function 

# a = 'Hello World'
# print(len(a)) 

# Check String :
    # To check the string contain a specific words or phrase we use in keyword . it return statement
    # in booleans values 

# txt = 'The best thing in life is memories'
# print('memories' in txt)

    # We can also verify it using if statement

# txt = 'The best thing in life is memories'
# if 'memories' in txt:
#     print('Yes Memories is Present')

# Check if not :
    # to check if a certain pharas or word is not in string than we use not in keyword . 

# txt = 'The best thing in life is memories'
# print('exoensive' not in txt)

    # we can also verify it using if statement 

# txt = 'The best thing in life is memories'
# if 'expensive' not in txt:
#     print('No expensive is not Present')

# SLICING STRING :
    # We can return a range of character by using slice syntax . Specify he first index , last index
    # separated by colon , to return a part of sring . The first character has index 0

# a = ' HELLO WORLD'
# print(a[2:7])

# Slice From Start :
    # by leaving out start index , the range will start at first character . The following example return
    # character from start to the 5 index , 5 is not included 

# a  = 'Hello World'
# print(a[:5])

# Slice From End :
    # By leaving out end index , the range will go to the end . The following example return character 
    # from start postion index and go to the end .

# a = 'Hello World'
# print(a[2 :])

# Negative Indexing :
    # We use negative indexing to start slicing from end of string
    # In the following example the slicing start from 'O' and goes to 'H'

# a = 'Hello World'
# print(a[-5 : -1]) 
# print(a[-5 : -2]) 


# MODIFY STRINGS 
    # Python has a set of built-in methods which is used to work / modify  string

a = 'Hello World'
# a = '    Hello World'
# a = 'Hello, World'

# 1 . Upper ():
    # The upper method is used to return string in upper case

# print(a.upper())

# 2. Lower():
    # The lower method is used to return string in lower case

# print(a.lower())

# 3 . Strip () :
    # Witespace is the spcae which is before/after of the actual text .To remove it we use strip method
    # in string

# print(a.strip())

# 4 . Replace() :
    # This method is used to replace a string with another one

# print(a.replace('World' , 'Morning'))

# 5 . Split():
    # This method is used to split string into substring if it finds the instance of separator

# print(a.split(','))

# STRING CONCATINATION :
    # To concatinate / Combine or add two sting we use '+' operator

# a = 'Hello'
# b = 'World'
# print(a + b)

    # To add space between them we have to add it separately

# print(a + " " + b)

# PYTHON FORMAT STRING 
    # As we learned with pyhon variable chapter string and integer can not combine like this :

# age  = 24
# txt = 'My name is Muzzi and Age is ' + age
# print(txt)

    # But we can combine string and numbers by using f-string 

# F-String :
    # F string was interduces in python 3.6 and now is prefered  way of formatting string
    # To specify a string as an f-sting . Simply put an f in front of string literal , and add curly
    # brackets {} as placeholder for variables and other operations .Like this :

# age = 25
# txt = f'Hi My Name Is Muzzi and Age is {age}'
# print(txt)   

# PLACEHOLDERS AND MODIFIERS :
    # A placeholder can contain variables , functions , operation and modifiers to format the value 
    # We add a placeholder for price variable

# price = 500
# txt = f'The price of this bottle is {price}'
# print(txt)

    # A placeholder can include a modifier to format the value
    # A modifier is included by adding a colon: followed by a legal formatting type , like .2f
    # which mean fixed point numbers with 2 decimal 
    
    # Display price with 2 decimal like this :

# price = 59
# txt = f'The price of this bottle is {price:.2f}'
# print(txt)

    # A placeholder can contain python code like math operation

# txt = f'The price is {20 * 40}'
# print(txt)

# PYTHON ESCAPE CHARACTERS 
    # To insrt characters that are illegal in a string so we use Escape characters
    # An Escape character is a backslash followed by a charcater we want to insert
    # An example of an illegal character is doule quote inside a string that is surrounded by 
    # double quotes . like this :

# txt = "We are the so-called "vi-kings" from the north"

    # To fix this problem we use \ escape characters 

# txt = "We are the so-called \"vi-kings\" from the north"

    # There  are several other escape characters in python .











