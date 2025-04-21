# PYTHON DICTIONARY:
    # Dictionary are used to store values in Key value pairs . A dictionary is a collection which is
# ordered , changeable and do not allow duplicate values .  

    # As of python 3.7 dictionary are ordered , in 3.6 and earlier dictionary are unordered . 
    # Dictionary are written in curly brackets , and contain key , value pairs .

# my_dict = {
#     "name" : 'Muzammil',
#     "age" : 20
# }  
# print(my_dict)

# DICTIONARY ITEMS :
    # Dictionary items are ordered , changeable and do not allow duplicate values .
    # Dictionary items are presented in key , value pairs and can be refferdby using key name 

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# }

# print(my_dict['name'])

# ORDERED OR UNORDERED ?
    # As of python 3.7 dictionary are ordered , in 3.6 and earliers dictionary are unordered .

    # When we say dictionary are ordered , it means that the items have a defined ordered , and that
# order will not change . 
    # Unordered means the items donot have a defined order , you can not refer to the items by using
# indexing 

# CHANGEABLE:
    # Dictionary are changeable , meaning that we can change , add or remove items from dictionary after 
# it is created . 

# DUPLICATES CAN NOT ALLOW :
    # Dictionary can not have 2 items with same keys . 

# car_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla",
#     "year" : 2015,
#     "year" : 2018
# }     
# print(car_dict)

# DICTIONARY LENGTH :
    # To determine the length of dictionary we use len() function . 

# car_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla",
#     "year" : 2018
# }
# print(len(car_dict))

# DICTIONARY ITEMS :
    # The values in dictionary can be of any datatypes . 

# my_dict = {
#     "brand" : "Toyota",
#     "Sun-roof" : True,
#     "year" : 2018,
#     "color" : ['red' , 'white']
# }
# print(my_dict)

# DICT () CONSTRUCTOR :
    # It is possible to use dict () constructor for creating dictionary

# my_dict = dict(name = 'Muzammil' , age = 20)
# print(my_dict) 

# ACCESS ITEMS :
    # We can access the items from dictionary by using key name , inside square brackets

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# }
# print(my_dict)

    # There is also a method called get() qwhich return same result

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# }
# print(my_dict.get('name'))

# GET KEYS () :    
    # The keys method return all keys present in dictionary

# my_dict = {
#     'name' : "Muzammil",
#     'age' : 20
# }
# print(my_dict.keys())

    # The list of key is the view of dictionary , meaning that if any changes made do the dictionary 
# it will be reflected on in the keys list .

# my_dict = {
#     "name" : 'Muzammil',
#     "age" : 20
# }

# print(my_dict.keys())

# my_dict['height'] = '6ft'

# print(my_dict.keys())

# GET VALUES():
    # The values() method will return list of all values in dictionary 

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# }
# print(my_dict.values())

    # The list of values is the view of dictionary , meaning that any changes made in the dictionary
# will be reflected on the values list 

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# }
# print(my_dict.values())

# my_dict["height"] = '6ft'

# print(my_dict.values())

# ITEMS ():
    # The get items() method will each item in dictionary as tuples in list 

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# }

# print(my_dict.items())

    # The return list is the view of the items in the dictionary , meaning that any changes done in
# the dictionary will be affected on values 

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# } 

# print(my_dict.items())

# my_dict['height'] = '6ft'

# print(my_dict.items())

# CHECK IF KEY EXISTS ?:
    # To determine the specified key present in the dictionary we use 'in' keyword .

# my_dict = {
#     "name" : "Muzammil",
#     "age" : 20
# }

# if 'age' in my_dict:
#     print('Yes age is present as key in dictionary')

# CHANGE VALUES :
    #  We can change specific values by referring its key name in dictionary . 

# my_dict = {
#     "name" : "Mzammil",
#     'year_of_birth' : 2005
# }
# my_dict["year_of_birth"] = 2000

# print(my_dict)

# UPDATE DICTIONARY :
    # We can update the values inside dictionary by using Update() method . 
    # The argument must be dictionary or an iterable object with key: value pairs 

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }
# my_dict.update({"'model" : "Vitz"})
# print(my_dict)

# ADDING ITEMS :    
    # Adding an item to the dictionary is done by using a new index key and assigning a value
# to it . 

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }
# my_dict['color'] = 'black'
# print(my_dict)

# UPDATE DICTIONARY :
    # The update () method will update the dictionary with the items from  a given arguments , if 
# the items is not exists it will add it 
    # The argument must be dictionary or any iterable objects with key , value pair 

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }     

# my_dict.update({'color' : "black"})
# print(my_dict)

# REMOVING ITEMS :
    # There are several methods to remove items from dictionary . 

# 1 . POP ():
    # The pop() method will remove items with specified key name 

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }

# my_dict.pop('model')
# print(my_dict)

# 2 . POPITEM ():
    # The pop items will remove the last inserted items (in version before 3.7 a random item is removed)

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }

# my_dict.popitem()
# print(my_dict)

# 3.  DEL ():
    # The del keyword will removes the item with sepecified key name 

# my_dict = {
#     "brand" : 'Toyota',
#     "model" : "Corolla"
# } 
# del my_dict['brand']

# print(my_dict)

    # The del keyword can also delete dictionary completely 

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }

# del my_dict
# print(my_dict)

# 4 . CLEAR ():
    # The clear () method is used to empty dictionary

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }
# my_dict.clear()

# print(my_dict)

# LOOP THROUGH A DICTIONARY 
    # We can loop through a dictionary using for loop 
    # When looping through a dictionary , the return values are the keys from dictionary , but there
# are methods to return values as well 

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla",
#     "color" : 'Black'
# }

    # Print all names of keys one-by-one

# for key in my_dict:
    # print(key)

    # We can also use keys () method to prints key from dictionary

# for keys in my_dict.keys():
#     print(keys)

    # Print all values from keys one-by-one

# for values in my_dict:
#     print(my_dict[values])

    # We can also use values() method to return values from dictionary

# for values in my_dict.values():
#     print(values) 

    # Loop through both key , values by using item() method

# for key , values in my_dict.items():
#     print(key , values)

# COPY DICTIONARY :
    # We can not copy dictionary by writing this 'dict1 = dict 2' because dict2 will be reference to 
# dict1 , and changes made in dict1 will also reflect on dict2
    # There are ways to make copy , one is to use built-in method copy()

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }

# new_dict = my_dict.copy()
# print(new_dict)

    # Another way is to make copy by using built-in function dict()

# my_dict = {
#     "brand" : "Toyota",
#     "model" : "Corolla"
# }

# new_dict = dict(my_dict)
# print(new_dict)

# NESTED DICTIONARY :
    # A dictionary can also contain dictionary , this method is called nested dictionary

# family = {
#     "child1" : {
#         "name" : "Ahmed",
#         'age' : 20
#     },
#     "child2" : {
#         "name" : "Rafay",
#         "age" : 16
#     },
#     "child3" : {
#         "name" : "John",
#         'age' : 12
#     }
# }

# print(family)

    # Or if we want to add three dictionary into new dictionary 

# child1 = {
#     "name" : "Ahmed",
#     "age" : 20
# },

# child2 = {
#     "name" : "Rafay",
#     'age' : 16
# }

# child3 = {
#     "name" : "John",
#     "age" : 12
# }

# new_dict = {
#     "child1" : child1,
#     'child2' : child2,
#     'child3' : child3
# }
# print(new_dict)

# ACCESS ITEMS IN NESTED DICTIONARY :
    # We can access items ion nested dictionary by using the name of dictionary starting from
# outer dictionary 

# family = {
#     "child1" : {
#         "name" : "Ahmed",
#         'age' : 20
#     },
#     "child2" : {
#         "name" : "Rafay",
#         "age" : 16
#     },
#     "child3" : {
#         "name" : "John",
#         'age' : 12
#     }
# }

# print(family["child1"]['age'])

# LOOP THROUGH NESTED DICTIONARY :
    # We can loop through nested dictionary by using items() method like this 

# family = {
#     "child1" : {
#         "name" : "Ahmed",
#         'age' : 20
#     },
#     "child2" : {
#         "name" : "Rafay",
#         "age" : 16
#     },
#     "child3" : {
#         "name" : "John",
#         'age' : 12
#     }
# }

# for keys , obj in family.items():
#     print(keys)

#     for values in obj:
#         print(values + ':' , obj[values])







