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

txt = 'The best thing in life is memories'
if 'expensive' not in txt:
    print('No expensive is not Present')








