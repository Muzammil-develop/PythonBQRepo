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

# new_list = ['Arham' , 'Khan' , 56 , False]
# if 56 in new_list:
#     print('Yes it is present in list')

# CHANGE ITEM VALUE :
    # To change the value of specific item we refer index number

# list_value = [1 , 5 , ' Arham' , 'Fan' , True]
# list_value[1] = 'Khan'
# print(list_value)

# CHANGE A RANGE OF ITEMS :
    # To change the value of items in a specific range , define a list with new values and refer 
# to the range of index numbers where you want to insert new values 

# list_value = [1 , 5 , ' Arham' , 'Fan' , True]
# list_value[1 : 3] = ['Tyre' , 'Cupboard']
# print(list_value)

    # If we insert more items than you replace , the new items will be inserted where you specified
# and the remaining item will move accordingly :

# list_value = ['arham' , 'pasha' , 2]
# list_value[1 : 2] = ['khan' , 55]
# print(list_value)  

# Note :
    # The length of list will be changed if the number of items inserted does not match with the item
# replaced

    # If we insert less item than we replace , the new item will be inserted where we specified , and
# the remainging item will move accordingly . 

# my_list = ['arham' , 'apple' , 'jar']
# my_list[1 : 3] = ['marks']
# print(my_list) 

# INSERT ITEMS :
    # To insert an items in list list without removing any existing values than we use insert() 
# method . 
    # The insert method is used to insert items at specified index

# list_item = [2, 4 , 6 , 'Grow' , True]
# list_item.insert(2 , 'Khan')
# print(list_item)  

# ADD LIST ITEMS :
# my_list = ['arham' , 'apple' , 'orange' , True]

# 1.  APPEND METHOD ():
    # To add an item at the end of list we use append() method

# my_list.append('Prize')
# print(my_list)

# 2. INSERT METHOD ():
    # To insert an item at a specified index we use insert() method

# my_list.insert(2 , 'kali')
# print(my_list) 

# 3. EXTEND METHOD ():
    # TO append elements from another list to current list we use extend() method.

# new_list = [456 , False , 'Cow']
# my_list.extend(new_list)
# print(my_list) 

# ADD ANY ITERABLE :
    # The extend() method does not have to append list , we can add any iterable object (tuples ,
# sets , dictionaries , etc)

# Now we add elements of tuple in list 

# new_tuple = ('Kahn' , 'pk' , 'lala')
# my_list.extend(new_tuple)
# print(my_list) 

# REMOVE LIST ITEM :

# 1. REMOVE METHOD(): 
    # The remove item is ued to remove specified item

# my_list.remove('orange')
# print(my_list)

    # If there are more than one values in specified item then it will remove the first
    # occurance

# my_list1 = ['apple' , 'banana' , 'orange' , 'banana']
# my_list1.remove('banana')
# print(my_list1)

# 2. POP METHOD ():
    # To remove items from specified index we use pop () method .

# my_list.pop(2)
# print(my_list) 

    # If we donot specify the index the pop method will remove elements from last index 

# my_list.pop()
# print(my_list)

# 3. DEL KEYWORD ():
    # The del keyword is also used to delete items at specified index

# del my_list[1]
# print(my_list)

    # The del keyword remove whole list if we donot specify the index

# del my_list
# print(my_list)

# 4. CLEAR METHOD :
    # The clear method is used to empty the list . it can not delete list , it just removes all 
# list items from it

# my_list.clear()
# print(my_list)

# LOOP THROUGH LIST :
    # we cn loop through the list item by using for loop .

# new_list = ['apple' , 'orange' , 'banana' , 'lemon']
# for items in new_list:
#     print(items)

# LOOP THROUGH INDEX NUMBER :
    # we can also loop through the items by using their index number . We use range() and len()
# function to make a suitable iterable.

# for i in range(len(new_list)):
#     print(new_list[i])

# USING A WHILE LOOP :
    # we can also loop through the items by using a while loop . 
    # use len() function to determine the length of the list , then start at 0 and loop your way
# through the list items by refering to their indexes . 
    # Remember to increase the +1 after each iteration

# new_list = ['apple' , 'orange' , 'banana' , 'lemon']
# i = 0
# while i < len(new_list):
#     print(new_list[i])
#     i += 1

# LOOP THROUGH LIST COMPREHENSION :
    # list comprehension offers the shortest syntax for looping through list:

# new_list = ['apple' , 'orange' , 'banana' , 'lemon']
# [print(x) for x in new_list]
   
# LIST COMPREHENSION :
    # list comprehension offers a shorter syntax when we want to create a new list based on the 
# values of an existing list .

# Example:
    # Based on the list of fruits , we want a new list , containing only the fruits with the letter 
# "a" in the name. withour list comprehension we have to write a for statement with a conditional
# test inside . 

# fruits = ['apple' , 'banana' , 'orange' , 'kiwi']
# new_list = []

# for fruit in fruits:
#     if 'a' in fruit:
#         new_list.append(fruit)

# print(new_list)

    # With list comprehension we can do this in 1 line of code .

# fruits = ['apple' , 'banana' , 'orange' , 'kiwi']

# new_list = [fruit for fruit in fruits if "a" in fruit]

# print(new_list)

# THE SYNTAX :

# new_list = [expression for item in iterable if condition == True]

# CONDITION :
    # The condition is like a filter that only accepts the item which is True

# new_list = [x for x in fruit if x != 'apple']

    # The condition if x != 'apple' will return True for all elements other than 'apple' making 
# the new list contain all fruits except apple
    # The condition is optional and can be omitted

# new_list = [x for x in fruits]

# ITERABLE :
    # The iterable can be any iterable object like list , tuple , sets etc

# new_list = [x for x in range(10)]
# print(new_list)

    # same example with a consition .
 
# new_list = [x for x in range(10) if x > 5]
# print(new_list)

# EXPRESSION :
    # The expression is the current item in the iteration , but it is also the outcome , which
# we can manipluate before it ends up like a list in new list .

# new_list = [x.upper() for x in fruits]

    # We can set the outcome whatever we like .

# new_list = ['Hello' for x in fruits]

    # The expression can also contains filter not like condition but as a way to manipulate outcome

# new_list = [x if x != 'banana' else 'orange' for x in fruits]

# The expression in the above statement says :
    # Return the item if it is not banana , if it is banana return orange

# SORT LIST :

# 1 .SORT LIST ALPHANUMERICALLY :
    # list object have a sort method that will sort list aplhanumeriacally , ascending ,by default:

# SORT LIST ALPHABATICALLY :
# new_list = ['Apple' , 'Mango' , 'Banana' , "Orange"]
# new_list.sort()
# print(new_list)

# SORT LIST NUMERICALLY:
# new_list = [100,56,15,230,5]
# new_list.sort()
# print(new_list)

# SORT DECENDING:
    # TO sort list decending we use a keyword called resverse=True

# new_list = ['Apple' , 'Mango' , 'Banana' , "Orange"]
# new_list.sort(reverse=True)
# print(new_list)

# new_list = [100,56,15,230,5]
# new_list.sort(reverse=True)
# print(new_list)

# CUSTOMIZE SORT FUNCTION :
    # We can also customize our sort function by using the keyword argument key = Function
    # The function will return a number that is used to sort the list(the lower number first)

# def myfunc(n):
#     return abs (n -50)

# new_list =  [100, 50, 65, 82, 23]
# new_list.sort(key=myfunc)
# print(new_list)

# CASE INSENSITIVE SORT:
    # be default sort is case-sensitive . resulting in all capital letters being sorted before lower 
# case letters

# new_list = ['Apple' , 'banana' , 'Orange' , 'mango']
# new_list.sort()
# print(new_list)

    # Luckily we can use a built-in function as a key function when sorting a list . 
    # So if we want a case-insensitive sort we use str.lower as a key function

# new_list.sort(key=str.lower)
# print(new_list)

# REVERSE ORDER :
    # If we want to reverse order of list  , regardless of alphabet .The reverse() method reverses the
# current order of the lsit

# new_list = ['Apple' , 'banana' , 'Orange' , 'kiwi']
# new_list.reverse()
# print(new_list)   

# COPY LIST :
    # If we want to copy the list we can not do this list1 = list2 , because list2 will only be a 
# reference to list1 . and changes made on list1 will automatically appear on list2

# 1 .USE COPT METHOD():
    # We can use a built-in list method copy() to copy a list

# my_list = ['Arham' , 55 , 'Fan' , False]
# list2 = my_list.copy()
# print(my_list , list2)

# 2 .LIST METHOD():
    # Another way to copy the list is using list method .

# my_list = ['Arham' , 55 , 'Fan' , False]
# list2 = list(my_list)
# print(my_list , list2)

# 3. USING SLICE OPERATOR :
    # We can also copy the list by using slicing

# my_list = ['Arham' , 55 , 'Fan' , False]
# list2 = my_list[:]
# print(my_list , list2)

# JOIN LIST :
    # There are several ways to join , concatinate two or more list .One of the easiest way by using "+"
# operator

# my_list = ['Arham' , 55 , 'Fan' , False]
# new_list = ['khybar' , 'board' , 85 , True]

# print(my_list + new_list)

    # Another way to join 2 list is by appending all items from list2 to list1 one-by-one

# my_list = ['Arham' , 55 , 'Fan' , False]
# new_list = ['khybar' , 'board' , 85 , True]

# for item in new_list:
#     my_list.append(item)

# print(my_list)

    # We can also use extend() method . where the purpose is to add 1 list from another list


# my_list = ['Arham' , 55 , 'Fan' , False]
# new_list = ['khybar' , 'board' , 85 , True]

# my_list.extend(new_list)
# print(my_list)





