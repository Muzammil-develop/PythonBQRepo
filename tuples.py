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