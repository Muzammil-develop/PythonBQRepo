# PYTHON ITERATORS :
    # An iterator is an object that contains a countable number of values. 
    # An iterator is an object that can be iterated upon , meaning that we can tranverse through all
# the values . 
    # Technically in python an iterator is an object which implements the iterator protocol , which 
# consist of the methods __iter__() and __next__().

# ITERATORS VS ITERABLE :
    # List , tuples, dictionary , and sets are all iterable object . They are iterable container which 
# we can get an iterator from 
    # All these objects have an iter() method which is used to get an iterator

# tuple_value = ('Apple' , 'Banana' , "Orange")
# my_iter = iter(tuple_value)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

    # Even strings are iterable objects and can returns an iterator

# fruit = "Banana"
# my_iter = iter(fruit)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# LOOPING THROUGH AN ITERATOR :
    # We can also use a for loop to iterate through an iterable object .

# fruits = ('apple' , 'banana' , 'orange')

# for fruit in fruits:
#     print(fruit)

    # Iterate characters of string 

# fruit = 'Banana'

# for var in fruit:
#     print(var)

    # The for loop actualy creates an iterator object and executes the next() method for each loop 

# CREATE AN ITERATOR :
    # To create and object/class as an iterator we have to implement the methods __iter__() and 
# __next__() to our object .
    # As we have learned in Python classes/ object chapter . All classes has a function  called __init__()
# which allow us to do some initializing when object is being created .
    # The __iter__() method acts similar , we can do operations (initializing etc) , but must always
#  return iterator object itself .  
    # The __next__() method allows us to do operations, and must return the next iterms in sequence .

# class Numbers:

#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
    
# c = Numbers()
# my_iter = iter(c)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# STOPITERATION :
    # The example above would continue if we have enough __next__() statements , or if it was used 
# in a for loop . 
    # To prevent the iteration from going on forever , we can use the StopIteration statement
    # In the __next__() method , we can add a terminating condition to raise an error if the iteration
# is done a specified number of times .

# class Number:

#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         if self.a <= 20:
#             # self.a += 1
#             # return self 
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
        
# c = Number()
# my_iter = iter(c)

# for values in my_iter:
#     print(values)



