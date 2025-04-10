# PYTHON BOOLEANS 
    # Boolean represents one of two values True Or False 

# BOOLEAN VALUES :
    # In Programming we often need to know if an expression is True or False 
    # You can evaluate any by expression in python and get one of two answer  , True or False
    # When you compare two values the expression is evaluated and Python returns Boolean answer

# print(10 > 9)
# print(10 == 10)
# print(10 < 9) 

    # When we run a condition in if statement it returns True or False . We print a message based on 
    # whether condition is True or False 

# a = 200
# b = 33

# if b > a:
#     print('b is greater than a')
# else:
#     print('b is not greater than a')

# EVALUATE VALUES AND VARIABLES 
    # The boolean function allow us to evaluate any value , and give us True or False in return 

# print(bool('Hello'))
# print(bool(15)) 

# MOST VALUES ARE TRUE 
    # Almost every values is evaluated to True if it has some sort of content . 
    # Any string is True , except empty string 
    # Any number is True , except 0
    #  Any list , tuple ,set , dictionary are True except empty one 

# print(bool(123))
# print(bool('str'))
# print(bool([1,2,8]))

# SOME VALUES ARE FALSE 
    # In fact there are not many values that evaluate to false , except empty values , such as () , [] ,
    # "" , , the number 0 , and the value none . And ofcourse the value false evaluated to false

# print(bool(False))
# print(bool(None))
# print(bool(0))

    # One more value or object in this case evaluates to false and that is if you have an object 
    # that is made from a class with __len__ function that returns 0 or False 

# class MyClass():

#     def __len__(self):
#         return 0
    
# obj = MyClass()
# print(bool(obj))

# FUNCTION CAN RETURN A BOOLEAN :
    # We can create a fucntion that returns a boolean value . like this"

# def MyFunction():
#     return True

# print(MyFunction())

    # We can execute a code based on boolean answer of a function .

# if it true  it print yes otherwise no

# if MyFunction():
#     print('Yes')
# else:
#     print("No")

    # Python also have many built-in function that returns a boolean value , like the isinstance() function
    # which can be used to determine if an object is on certain datatype . 

# x = 200
# print(isinstance(x,int)) 





