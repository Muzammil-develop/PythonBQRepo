# PYTHON INHERITANCE :
    # Inheritance allows us to define a class that inherits all the properties and methods from another
# class . 

# Parent Class is the class being inherited from 
# Child Class is the class that inherits from another class , also called derived class .

# CREATE A PARENT CLASS :
    # Any class can be parent class so the syntax is the same as creating any other class.

class Person:

    def __init__(self ,name , age):
        self.name = name
        self.age = age

    def func(self ):
        print('Your Name is ' + self.name)

    
p = Person('John' , 25)
p.func()

# CREATE A CHILD CLASS :
    # To create a cass that inherits the functionality from another class , send the parent class as 
# the parameter when creating the child class

# class Student(Person):
#     pass

# NOTE :
    # Use the pass keyword when we donot want to add any other properties and methods to the class

    # Now the student class has the same properties and methods as the Person class

# x = Student('Mike' , 40)
# x.func()

# ADD init FUNCTION :
    # So far we have created a child class that inherits the properties and methods from its parent class
    
    # So we have to add __init__() function to the child class (instead of the pass keyword).

# NOTE :
    # The __init__() function call automatically the class is being used to create a new object .

# class Student(Person):

    # def __init__(self):
        # pass      

    # Whn we add the __init__() function the child class will no longer inherits the parent __init__()
# function

# NOTE :
    # The child __init__() function overrides the the inheritance of parents __init__() function .
    
    # To keep the inheritance of the parent __init__() function .add a call to the parents __init__()
# function 

# class Student(Person):

#     def __init__(self):
#         Person.__init__(self)

    # Now we have successfuly added the __init__() function , and kept the inheritance of the parent 
# class , and we are ready to add functonality in the __init__() function .

# SUPER FUNCTION :
    # Python also has a super function() that will mae the child class inherits all the methods and
# properties from its parent :     

# class Student(Person):

#     def __init__(self, name, age):
#         super().__init__(name, age)

    # By using super() function we do not have to use the name of the parent element , it will 
# automatically inherit the methods and properties from its parent .













