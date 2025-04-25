# NOTE :
    # Python does not have built-in support for Arrays . instead Python list can be used . 

# ARRAYS :
    #  Arrays are used to store multiple values in 1 single variable like

# car = ['Toyota' , 'Honda' , 'Volvo']

# WHAT IS AN ARRAY :
    # An array is a special variable which csan hold one value at a time .
    
    # If we have a list of item (a list of car namesfor example) , storing the cars in single variable 
# could look like this :

# car1 = 'Toyota'
# car2 = 'Honda'
# car3 = 'Volvo'

    # However if we want to loop through the cars and find a specific one ? and what if we have not 3 
# car but 300 ?
    # The solution is Array
    # An array can hold many values under a single name , and we can access this values by referring
# to an index number .

# ACCESS THE ELEMENTS OF AN ARRAY :
    # we can refer to an array elements by referring a index number 

# cars = ['Toyota' , 'Honda' , 'Volvo']
# print(cars[1])     

    # We can also modify the values of first array items .

# cars[0] = 'Ferrari'
# print(cars) 
 
# LENGTH OF ARRAY :
    # We can use len() function to find the length of array

# cars = ['Toyota' , 'Honda' , 'Volvo']
# print(len(cars)) 

# NOTE:
    # The length of array is always come one more thn the highest array index .

# LOOPING ARRAY ELEMENTS :
    # we can use for in loop to loop through all elements of an array 

# cars = ['Toyota' , 'Honda' , 'Volvo']
# for car in cars:
#     print(car)

# ADDING ARRAY ELEMENTS :   
    # We can use append() method to add an element to an array

# cars = ['Toyota' , 'Honda' , 'Volvo']
# cars.append('Ferrari')
# print(cars)

# REMOVING ARRAY ITEMS :
    # We can use the pop() method to remove an element from an array

# cars =['Toyota' , 'Honda' , 'Volvo']
# cars.pop(1)
# print(cars)

    # We can also use remove method to remove items from an array

# cars.remove('Volvo')
# print(cars)

# NOTE :
    # The list remove method only removes the first occurance of the specified value
















