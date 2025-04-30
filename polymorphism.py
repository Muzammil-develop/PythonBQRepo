# POLYMORPHISM:
    # The word ploymorphism means 'many forms' and in programming it refers to methods / functions
# operators with the same name that can be executed on many objects or classes . 

# FUNCTION POLYMORPHISM :
    # An example of python function that can be used on different objects is the len() function 

# 1 . String:
    # For string len() returns number of characters .

# x = "Hello World"
# print(len(x))

# 2 . Tuple:
    # For tuple len() returns number of items in the tuple

# x = ('Apple' , 'Banana' , 'Orange')
# print(len(x))

# 3 . Dictionary :
    # For dictionary len() returns the number of key/value pairs in the dictionary

# my_dict = {
#     'name': "Muzammil",
#     "age" : 25
# }

# print(len(my_dict))

# CLASS POLYMORPHISM :
    # Polymorphism is often used in the class methods where we can have multiple classes with same method
# name for example , say we have three classes Car , Boat , Plane , and they all have a method called 
# move():

# class Car:

#     def __init__(self, brand , model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print('Drive')

# class Boat:

#     def __init__(self , brand , model):
#         self.brand = brand 
#         self.model = model

#     def move(self):
#         print('Sail')

# class Plane:

#     def __init__(self , brand , model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print('Fly')

# car1 = Car('Ford' , 'Mustang')
# boat1 = Boat('Ibiza' , 'Touring 20')
# plane1 = Plane('Boeing' , 747)

# for x in (car1 , boat1 , plane1):
#     print(x.move())

    # Look at the for loop at the end . Because of polymorphism we can execute the same method for all
# three classes .

# INHERITANCE CLASS POLYMORSPHISM: 
    # What about classes with child class with the same name , Can we use polymorphism there ?
    # Yes if we use the example above and make a parent class called vehicle and make Car , Boat , Plane
# child classes of vehicle ,the child class inherits the Vehicle method but can override them .

# class Vehicle:

#     def __init__(self , brand , model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print('Move')

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):

#     def move(self):
#         print('Sail')

# class Plane(Vehicle):

#     def move(self):
#         print('Fly')

# car1 = Car('Ford' , 'Mustang')
# boat1 = Boat('Ibiza' , 'Touring 20')
# plane1 = Plane('Boeing' , 747)

# for x in(car1 , boat1 , plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()

    # Child class inherits the properties and methods from parent class . 
    # In the example above we can see that car class is empty , but it inherits brand , model , move ()
# from vehicle 
    # The boat and plane classes also inherit brand , model , move() from vehicle but they both override
#  the move() method .
    # Because of polymorphism we can execute the same method for all classes .

