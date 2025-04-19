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

my_dict = {
    "name" : "Muzammil",
    "age" : 20
}

if 'age' in my_dict:
    print('Yes age is present as key in dictionary')






















