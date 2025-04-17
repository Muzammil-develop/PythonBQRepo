# SETS : 
    # Sets are used to store multiple items in a variable . 
    # Set is one of the nuilt-in datatypes in python used to store collection of data , the other 3 
# are lists ,tuples , dictionary . All with different qualities and usage .
    # A set is a ollection which is unordered , unchangeable and unindexed .
    
# NOTE :
    # Set items are unchangable but we can add , remove an items 
    
    # Sets is denoted by curly brackets {}

# my_set = {2 , 4, 6}
# print(my_set)      

# NOTE:
    # Sets are unordered so we can not sure which order the items will appear.

# SET ITEMS :
    # Set items are unordered , unchangeable and donot allow duplicate values .

# UNORDERED:
    # Unordered means the items in a set does not have a defined order
    # Sets items can appear in a different order at each time when we call them and can not
# referred by index number or keys .

# UNCHANGEABLE:
    # Sets items are not changeable once it is assigned at the time of creation .
    # Once sets is created we can not change its items , but we can remove and add new values.

# DUPLICATES NOT ALLOWED :
    # Sets can not have same items with same values , there is no duplication possible. If
    # Duplicates are found , they will be ignored .

# my_set = {2 , 4 , 6 , 2 , 8}
# print(my_set)    

# NOTE :
    # The value 'True' , 1 are considered as same values and it will be treated as duplicates .

# my_set = {1, 2, 4 ,3 , True , "str"}
# print(my_set)

# NOTE:
    # The values 'False' and 0 are considered as same values and it will be treated as duplicates.

# my_list = {0 ,2 ,3 ,5 ,1 ,False ,'str'}
# print(my_list)

# GET LENGTH OF SETS:
    # To find length of sets we use len() function

# my_set = {2 ,4 , 6 , 8}
# print(len(my_set))

# SET ITEM DATATYPES :
    # Set items can be of any datatypes

# my_set1 = {1 ,2 ,4 , 8 , 5}
# print(my_set1)

# my_set2 = {'apple' , 'banana' , 'orange'}
# print(my_set2)

# my_set3 = {True , False}
# print(my_set3)

    # A set can also contain different datatypes.

# my_set = {'apple' , 2 , 4 , 8 , True}
# print(my_set)

# THE SETS CONSTRUCTOR():
    # It is also possible to use set constructor () to make a set

# my_set = set(('apple','banana','orange'))
# print(my_set) 

# ACCESS SETS ITEMS :
    # We can not access the items in sets by using index number or keys .
    # But we can use for loops to iterate over sets or put a condition that specified value
# is present by usinh 'in' keyword.  

# my_set = {"apple" , 'banana' , 'orange'}
# for fruit in my_set:
#     print(fruit)

# my_set = {"apple" , 'banana' , 'orange'}
# print('banana' in my_set)

    # WE can also use not in keyword .

# my_set = {'apple' , 'banana' , 'orange'}
# print('banana' not in my_set)

# ADD ITEMS :
    # Once a set is created . We can not change its item but we can add new items in it .

# 1 . ADD():
    # To add 1 item in set we use add() function

# my_set = {'apple' , 'banana' , 'orange'}
# my_set.add('mango')
# print(my_set)

# 2 . UPDATE ():
    # To add items from another set into current set we use update() method

# my_set = {'apple' , 'banana' , 'orange'}
# new_set = {'kiwi', ' mango'}
# my_set.update(new_set)
# print(my_set)

# ADD ANY ITERABLE :
    # The object in Update() method does not have to be set . It can be list , tuple , dictionary etc

# my_set = {'apple' ,'orange' , 'banana'}
# new_list = [2 , 5]

# my_set.update(new_list)

# print(my_set)

# REMOVE ITEM : 
    # To remove items from set we use remove() and discard() method .

# my_set = {'apple' , 'banana' , 'orange'}
# my_set.remove('banana')
# print(my_set)

# NOTE:
    # If the item to be removed isa not exists . It throw an error.

# my_set = {'apple' , 'banana' , 'orange'}
# my_set.discard('orange')
# print(my_set)

# NOTE:
    # If the item to be delete is not exists , it will not throw error

    # We can also use pop() method to remove an item  but this method will remove a random
# item , so we can not know which item is removed 

    # The return of pop items is the removed item

# my_set = {'apple' , 'banana' , 'orange'}
# my_set.pop()

# # OR 
# # x = my_set.pop
# # print(x)

# print(my_set)

    # The clear method empties the whole sets

# my_set = {'apple' ,'banana' , 'orange'}
# my_set.clear()
# print(my_set)

# OR 

# print(my_set.clear())

    # The del keyword delete the set permanentely

# my_set = {'apple' , 'banana' , 'orange'}
# del my_set
# print(my_set)


