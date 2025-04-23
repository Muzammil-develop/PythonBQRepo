# WHILE LOOPS :
    # Python has 2 primitive loop commands .

# 1. While loops
# 2. for loops

# WHILE LOOP :
    # With while loop we can execute a set of statement as long as condition is True

# i = 1
# while i < 6:
#     print(i)
#     i += 1

    # Remember to increment i otherwise loop will continue forever.
    # The while loop required relevant variables to be ready , in this example we need to define an
# indexing variable i , which is set to 1.

#  BREAK STATEMENT : 
    # With the break statement we can stop the loop even if the while condition is True

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# CONTINUE STATEMENT :
    # with the continue statement we can stop the current iteration and continue with the next .

# i = 0
# while i < 6:
#     i += 1 
#     if i == 3:
#         continue
#     print(i)

# ELSE STAEMENT :
    # with the else statement we can run a block of code once when condition no longer is True.

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# else:
#     print('i is no longer less than  6')

# FOR LOOP:
    # A for loop is is used to iterating over a sequence that is over(list , tuple , dictionary , set 
# or a string)  . 
    
    # This is less like the for keyword in othyer programming languages . and works more
# like an iterator method as found in other object oriented programming languages .

    # With the for loop we can execute a set of statements , once for each item in a list ,tuple,
# set , etc 

# fruits = ['apple' , 'banana' , 'orange']
# for fruit in fruits:
#     print(fruit)        

    # The for loop is not required an indexing variable to set beforehand

# LOOPING THROUGH STRINGS:
    # Even strings are iterable objects , they contain a sequence of character

# for x in 'banana':
#     print(x)

# BREAK STATEMENT :
    # with break statement we can stopped the loop before it has looped through all the items .

    # 1. Exit loop when fruit is banana

# fruits = ['apple' , 'banana' , 'orange']

# for fruit in fruits:
#     print(fruit)
#     if fruit == 'banana':
#         break

    # 2. Exit loop when x is banana , but this times break come before print . 

# fruits = ['apple' , 'banana' , 'orange']

# for fruit in fruits:
#     if fruit == 'banana':
#         break
#     print(fruit)

# CONTINUE STATEMENT :
    # With the continue statement we can stop the current iteration of the loop . and continue
# with the next .

# fruits =['apple' , 'banana' , 'orange']
# for fruit in fruits:
#     if fruit == 'banana':
#         continue
#     print(fruit)    

# RANGE FUNCTION :
    # To loop through a set of code a specified number of times , we can use range() function .
    
    # The range function returns a sequence of numbers , starting from 0 by default , and increments 
# by 1 (by default) and end as a specified number

# for i in range(6):
    # print(i)   

# NOTE :
    # The range (6) is not vqlues from 0 to 6 , but the values 0 to 5
    
    # The range function defaults to 0 as a starting value . however it is possible to specify the 
# starting value by adding a parameter range(2 , 6) which means value from 2 to 6 (but not including 6)       
    
# for x in range(2 , 6):
#     print(x)

    # The range function defaults to increment the sequence by 1 . however it is possible to specify the
# increment value by adding a third parameter range (2 , 20 , 2)

# for x in range(2 , 20 , 2):
#     print(x)

# ELSE IN FOR LOOP :
    # The else keyword in a for loop specifies a block of code to be executed when the loop is finished.

# for x in range(5):
#     print(x)
# else:
#     print('Loop is finished')

# NOTE: 
    # The else block will not executed if the loop is stopped by a break statement . 

# for x in range(5):
#     if x == 3:
#         break
#     print(x)

# else:
#     print('Loop is finished')

# NESTED LOOP :
    # A nested loop is loop inside a loop .

    # The inner loop will be executed one tiem for each iteration of the 'outer loop' 

# fruits = ['apple' , 'banana' , 'orange']
# names = ['ahmed' , 'moiz' , 'taha']

# for fruit in fruits:
#     for name in names:
#         print(fruit , name)

# PASS STATEMENT :  
    # for loops can not be empty , but if we want for a some reason to be empty , put the pass statement
# to avoid an error . 

# for x in [0,1,2]:
#     pass











