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

# SETS LOOPS:
    # We can loop through set items by using for loop .

# my_set = {"apple" , 'banana' , 'orange'}
# for items in my_set:
#     print(items) 

# JOIN SETS:
    # There are several ways to join 1 or more sets . 
    # The union() and update() method joins all items from both sets .
    # The intersection() method keeps only duplicates .
    # The difference() method keeps the item from 1 set that are not present in 2 set
    # The symmetric_difference () methods keep all items except duplicates.

# 1. UNION():
    # The union method returns new sets after combining 1 or more sets

# fruits = {'apple' , 'orange' , 'mango'}
# fruits2 = {'banana' ,'apple' , 'kiwi'}

# print(fruits.union(fruits2))

    # We can also use | operator instead of union .

# fruits = {'apple' , 'orange' , 'mango'}
# fruits2 = {'banana' ,'apple' , 'kiwi'}
# print(fruits | fruits2)

# JOIN MULTIPLE SETS:
    # All the joining methods and operators can be used to join multiple sets. 
    # When using a method , just add more sets in parenthesis , separated by comma 

# set1 = {"a" , 'b' , ' c'}
# set2 = {1 , 2 , 3}
# set3 = {'John' , 'Elia'}
# set4 = {True , False}

# new_set = set1.union(set2 , set3 , set4)
# print(new_set)

    # When usinh the | operators separate sets with more | operator

# set1 = {"a" , 'b' , ' c'}
# set2 = {1 , 2 , 3}
# set3 = {'John' , 'Elia'}
# set4 = {True , False}

# new_set = set1 | set2 | set3 | set4
# print(new_set)

# JOIN SETS AND TUPLE :
    # The union() method allows us to join sets with other datatypes . lik list or tuples. The
# result will be set .

# my_set = {'apple' , 'a' , 5}
# my_tuple = ('banana' , 8)

# print(my_set.union(my_tuple))

# NOTE:
    # The | operators only allow us to join sets with sets , not with other datatypes like you can
# with union . 

# 2 . UPDATE():
    # The update () method insert all items from 1 sets to another . The updates change the original
# sets and does not return new set .

# set1 = {2 , 4 , 6}
# set2 = {1 , 3 , 5}

# set1.update(set2)
# print(set1)

# NOTE:
    # Both union and update method exclude duplicate values .

# INTERSECTION:
    # The intersection() methods return a new set , that only contains a item that are present
# in both sets .

# set1 = {2 , 4 , 6 , 8 , 10}
# set2 = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}

# print(set1.intersection(set2))

    # We can also use & operator instead of intersection() method .

# set1 = {2 , 4 , 6 , 8 , 10}
# set2 = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}

# print(set1 & set2)

# NOTE :
    # The & operator only allows you to join sets with sets not with other datatypes like in
# intersection method .

    # Te intersection_update() method can only return duplicates values . but it will chang the original set
# instead of returning new set

# set1 = {2 , 4 , 6 , 8}
# set2 = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8}

# set1.intersection_update(set2)

# print(set1)

    # The value Trur and 1 treat as same value , also same for False and 0

# set1 = {'apple' , 1 , 'banana' , 0}
# set2 = {'john' , True , 'kiwi' , False}

# set1.intersection(set2)
# print(set1)

# 3 . DIFFERENCE():
    # The difference() method will return a new set that will only contains item from 1 set that
# are not present in other set 

# set1 = {'ahmed' , 'john' , 'rafay'}
# set2 = {'kali' , 'ahmed' , 'lala'}

# print(set1.difference(set2))

    # We can use the - operator instead of difference () method and get same result .
     
# set1 = {'ahmed' , 'john' , 'rafay'}
# set2 = {'kali' , 'ahmed' , 'lala'}

# print(set1 - set2)

# NOTE: 
    # The - operators will only allows to join sets with sets  and not with other datatypes . like
# with difference method .

    # The difference_update() method returns the element from 1 set which are not present in other set
# but it will make change in original set instead of returning a new set .

# set1 = {'ahmed' , 'john' , 'rafay'}
# set2 = {'kali' , 'ahmed' , 'lala'}

# set1.difference_update(set2)

# print(set1)

# 4 . SYMMETRIC_DIFFERENCE():
    # The symmetric_differnece method will keep only that elements which are not present in both set

# set1 = {'ahmed' ,'apple' , 'banana'}
# set2 = {'ahmed' , 'banana' , 'mango'}

# print(set1.symmetric_difference(set2))

    # We can use ^ operator instead of symmetric_difference() method and get the same result

# set1 = {'ahmed' , 'apple' , 'banana'}
# set2 = {'ahmed' , 'banana' , 'mango'}

# print(set1 ^ set2)

# NOTE:
    # The ^ operator will only allows us to join sets with sets and not with other datatypes just like 
# in symmetric_difference () method .

    # The symmetric_difference_update () method will also keep all elements except duplicates . but
# it will make changes in original set and will not retrun in new set

# set1 = {'apple' , 'banana' , 'orange'}
# set2 = {'ahmed' , 'banana' , 'kiwi'}

# set1.symmetric_difference_update(set2)
# print(set1)







