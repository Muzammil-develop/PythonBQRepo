# PYTHON COLLECTION :
    # There are four collection of datatypes in python . They are
    
# 1 . List:
    # List is collection which is ordered , changeable . Allow duplicate values

# 2 . Tuple:
    # Tuple is a collection which is ordered , unchangeable . Allow duplicate values 
    
# 3 . Sets :    
    # Sets is a collection which is unordered , unchangeable , and unindexed . No duplicate values
    
# 4 . Dictionary:
    # Dictionary is a collection which is ordered and changeable . No duplicate member .

# NOTE :  
    # Sets items are unchangeable but we can add and remove values whenever we want .              

# PYTHON LIST:
    # List are used to store multiple items in a single variable
    # List are one of the 4 built-in datatypes in python used to store collection of data , the other
    # 3 are Tule , Sets and Dictionary all with differnet qualities and usage .
    # List are created with [] brackets . like this

# name_list = ['Arham' , 'Ahmed' , 'Ayyan']
# print(name_list)

# LIST ITEMS:
    # List items are changeable and allow duplicate values .
    # List items are indexed , the index of first item is 0 and second item is 1

# LIST ORDER :
    # When we say list are ordered it means that the items have a defined order , and that order will 
    # not be changed .
    # If we add a new item to a list . it will be added at the end of the list 

# NOTE :    
    # There are some methods that will change the order of list but in general the order of
    # list is not changed

# CHANGEABLE :
    # The list is changeable which means the items in list can be add / update / delete after
    # the list is created

# LIST DUPLICATES :
    # Since list are ordered it can allow duplicate values in it . like this 

# name_list = ['Arham' , 'Ahmed' , 'Ali' ,'Arham']
# print(name_list)            

# LIST LENGTH :
    # To find the number of elements presents in list we have a function called len () . It prints
    # the number of length

# name_list = ["Arham" , 'Ahmed' , 'Ali']
# print(len(name_list))

# LIST ITEM - DATATYES :
    # List items can be of different datatypes

# list_str = ["Arham" , 'Ahmed' , 'Ali']
# list_int = [1,22,3,45]
# list_bool = [True , False]

# print(list_str)
# print(list_int)
# print(list_bool)

    # A single list can contain different datatypes . like this :

# list_data = ["Arham" , 2 , True]
# print(list_data)

# THE LIST CONSTRUCTOR ():
    # The list constructor can be used to create a new list. like this :

# new_list = list(('apple' , 'banana' , 'orange')) 
# print(new_list)

# PYTHON ACCESS LIST ITEM :
    # List items are indexed and we can access it used indexing. Remember the first indexing
    # start with 0 . like this

# list_item = ['Arham' , 2 , True]
# print(list_item[0])

# NEGATIVE INDEXING :
    # Negative indexing means start from end so -1 refers to the last items and so on .like this

# print(list_item[-1])

# RANGE OF INDEXES :
    # We can specify the range of indexes by specifying where to start and where to end .
    # When specify the range , the return values will be a new list with specified items

# fruits = ['apple' , 'mango' ,'banana' , 'orange' , 'pineapple']
# print(fruits[2:4])

    # The search will start at index 2 and end at 5 (not included)

# By Leaving out start values the range will start at zero . 

# print(fruits[ : 4])

# By leaving out the end values the range will go to the end of list

# print(fruits[2 :])

# RANGE OF NEGATIVE INDEXES :
    # Specify negative indexes if we want to start search from the end of list

# range_list = ['Arham' , 'Ahmed' , 5 , True]
# print(range_list[ -4 : -1])

# This return values from Arham (included) to True (not included)

# CHECK IF ITEM EXIST :
    # To specify the item present in list or not we use 'in' keyword . like this :

new_list = ['Arham' , 'Khan' , 56 , False]
if 56 in new_list:
    print('Yes it is present in list')


