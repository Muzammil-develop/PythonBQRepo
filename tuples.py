# PYTHON TUPLES :   
    # Tuples are used to store multiple values inside a single variable
    # Tuple is one of 4 built-in datatypes in python used to store collection of data , the other 3 are
# list , dictionary , sets . all with different qualities and usage 
    # A tuple is a collection which is ordered and unchangeable
    # Tuples are written with wrong bracket . like this :

# my_tuple = ('kiwi' , 'orange')
# print (my_tuple)

# TUPLE ITEMS :
    # Tuple items are changeable and allow duplicate values 
    # Tuple items are indexed , the first item have index 0 , the second one have 1

# ORDERED :
    # When we say that tuples are ordered . it means that the items have a defined order . the order can 
# not be changed

# UNCHANGEABLE:
    # Tuples items are unchangeable means we can not change , add , remove items from tuple after it has
# been created 

# ALLOW DUPLICATES :
    # Since tuple items are indexed , they can have items with same values .

# my_tuple = ('apple' , 'banana' , 'kiwi' , 85)
# print(my_tuple)

# TUPLE LENGTH:
    # To determine the length of tuple we use len() function

# my_tuple = ('apple' , 'banana' , 'kiwi' , 85)
# print(len(my_tuple))

# CREATE TUPLE WITH ONE ITEM :
    # To create a tuple with one item we have to add comma ',' after the item . otherwise python\
# will not recongnize it as a tuple

# my_tuple = ('Ayyan',)
# print(my_tuple , type(my_tuple))

# my_tuple = ('Ayyan')
# print(my_tuple , type(my_tuple))

# TUPLE ITEM  DATATYPE :
    # Tuple item can be of any datatypes.

# tuple1 = ('String' ' Int' , "floats values")
# print(tuple1)

# tuple2 = (45,82,5,7)
# print(tuple2)

# tuple3 = (True , False)
# print(tuple3)

    # A Tuple can contain differnet datatypes . 

# new_tuple = ('Ayyan' , 45 , True)
# print(new_tuple)


# TYPE():
    # From python prespective tuples are defined as a object with type tuple

# new_tuple = ('Ayyan' , 45 , True)
# print(type(new_tuple))

# TUPLE CONSTRUCTOR():
    # It is possible to use tuple constructor to make a tuple

# new_tuple = tuple(('apple' , 'banana' , 'orange'))
# print(new_tuple)

# ACCESS TUPLE ITEMS :
    # We can access the items of tuple by accessing their index numbers in square brackets

# new_tuple = ('Apple',  'banana' , 'cherry')
# print(new_tuple[1]) 

# NEGATIVE INDEXING:
    # Negative indexing means the starts from end , -1 refers to last item and -2 refers to
# second last item .

# new_tuple = ('Apple',  'banana' , 'cherry')
# print(new_tuple[-1])

# RANGE OF INDEXES :
    # We can specify the range of indexes by specifying where to start and where to end the range . 
    # When specifying the range the return value will be a new tuple with specified items

# new_tuple = ('Apple',  'banana' , 'cherry' , 'kiwi' , 'pineapple')
# print(new_tuple[2:4])

# NOTE:
    # The search will start at index 2 and end at 5 (not included)

    # By leaving out the start value , the range will start at the first item

# new_tuple = ('Apple',  'banana' , 'cherry' , 'kiwi' , 'pineapple')
# print(new_tuple[: 5])


    # By leaving out the end value , the range will go to end item

# new_tuple = ('Apple',  'banana' , 'cherry' , 'kiwi' , 'pineapple')
# print(new_tuple[2 : ])

# RANGE OF NEGATIVE INDEXES :
    # Specify the negative indexes if we want to start search for last element

# new_tuple = ('Apple',  'banana' , 'cherry' , 'kiwi' , 'pineapple')
# print(new_tuple[-3 : -1])

# CHECK IF ITEM EXISTS :
    # To check f items exists in tuple we use 'in' keyword

# new_tuple = ('Apple',  'banana' , 'cherry' , 'kiwi' , 'pineapple')
# if 'banana' in new_tuple:
#     print('Yes it is present')

# UPDATE TUPLES:
    # Tuples are unchangeable , means we can not change , add or remove items once tuple is created . 
# But  there are some workarounds 

# CHANGE TUPLE VALUES:
    # If we want to change the values of tuple . we have to first convert it into list , then change
# values and then convert it back into tuple .

# fruits = ('apple' , 'mango' , 'banana')
# list_view = list(fruits)
# list_view[1] = 'kiwi'

# result = tuple(list_view)
# print(result)

# ADD ITEMS :
    # Since tuple are immutable so they donot have built-in append method() . but there are other
# ways to add items to tuple 

# 1. CONVERT INTO LIST():
    # Just like the workaround for changing tuple , we can convert it into list , add our items and
# convert it back into tuples .

# fruits = ("apple" , 'orange' , 'banana')
# my_list= list(fruits)

# my_list.append('mango')
# result = tuple(my_list)

# print(result)

# 2. ADD TUPLE TO TUPLE :
    # We are allowed to add tuples to tuples, so if we want to add one or more items , create a new 
# tuple with the items and add it into existing tuple .

# fruits = ('apple' , 'banana' , 'orange')
# new_fruits = ('mange' , 'kiwi')

# print(fruits + new_fruits)

# NOTE :
    # When created a new tuple with single item donot forgot to add , at the end of items . otherwise
# It can be considered as string not tuple 

# REMOVE ITEMS :
    # We can not remove items from tuple , but we can follow same procedure which we follow to add
# items  in tuple , to remove elements from it .

# fruits = ('apple' , 'banana' , 'orange')
# my_list = list(fruits)

# my_list.remove('apple')

# result = tuple(my_list)
# print(result)

    # We can completely delete tuples if we want by using del keyword .

# fruits = ('apple' , 'banana' , 'orange')
# del fruits
# print(fruits)

# UNPACK TUPLES :
    # When we create a tuple we normally assign values to it . This is called packing a tuples.

# fruits = ('apple' , 'banana')

    # But in python we are also allowed to extract values back into variables . This is called
# Tuple unpacking

# fruits = ('apple' , 'banana')
# a , b = fruits

# print(a)
# print(b)

# NOTE :
    # The number of variables must match the number of values in the tuple , if not we must use
# an asterisk to collect the remaining values as a list.

# USING ASTRISK:
    # If the number of variables is less than the number of values , we can add asterisk to the 
# variables name and the values will be assigned to the variable as a list .

# fruits = ('apple' , 'banana' , 'mango' , 'orange')
# a , b ,*c = fruits

# print(a)
# print(b)
# print(*c)

    # If the asterisk is added to another variable name than the last , python will assign values
# to the variable until the numbers of values left matches the number of variables left.

# fruits = ('apple' , 'banana' , 'mango' , 'orange')
# a,*b,c = fruits

# print(a)
# print(*b)
# print(c)

# LOOP TUPLES :
    # We can loop through tuple items by using for loop

# fruits = ('apple' , 'banana' , 'orange')
# for fruit in fruits:
#     print(fruit)

# LOOP THROUGH INDEX NUMBERS:
    # We can also loop through itmes by referring to index numbers .
    # We use range() and len() function to create a suitable iterable .

# fruits = ('apple' , 'banana' , 'orange')
# for items in range(len(fruits)): 
#     print(fruits[items])

# WHILE LOOP :
    # We can loop through the tuple items by using while loop . 
    # Use len function to determine the length of tuple , then start at 0 and loop your way
# through tuple items by referring to their indexes . 
    # Remember to increase index number after each iteration

# fruits = ('apple' , 'banana' , 'orange')

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i = i + 1

# JOIN TUPLES :
    # To join two or more tuples we use '+' operator .

# fruits = ('apple' , 'banana' , 'orange')
# fruits2 = ('kiwi' , 'mango')
# print(fruits + fruits2)

# MULTIPLY TUPLES :
    # If we want to multiply the content of the tuple a given number of times , then we use '*'
# operator .

# fruits = ("apple" , "banana" , "orange")
# print(fruits * 2) 









