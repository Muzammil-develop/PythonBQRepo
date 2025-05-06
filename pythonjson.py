# PYTHON JSON :
    # Json is a syntax for stroing and exchanging data 
    # Json is tex written in Javascript object notation 

    # Python has a built-in package called json , which can be used to work with JSON data

# import json

# PARSE JSON CONVERT FROM JSON TO PYTHON :
    # if we have a json string we can parse it by using json.loads() method

# import json

# x = '{"name" : "Muzammil","age" : 19}'

# y = json.loads(x)

# print(y['name'])

# CONVERT FROM PYTHNO TO JSON :
    # If we have a python object , w can convert it into a JSON string by using the json.dumps() method.

# import json

# x = {
#     'name' : 'Muzammil',
#     'age' : 20
# }

# y = json.dumps(x)

# print(y)

# CONVERT PYTHON DIFFERENT OBJECTS INTO JSON 

# import json

# print(json.dumps({'name' : "John" ,'age' : 19}))
# print(json.dumps(['apple' , 'banana']))
# print(json.dumps(('apple' , 'banana')))
# print(json.dumps('hello'))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

    # When we convert from Python to json , python objcts are converted into the json (javascript) 
# equivalent

# import json

# x = {
#     "name" : "John",
#     "age" : 20,
#     "married" : True,
#     "divorced" : False,
#     "children" : ('Aun' , 'Killey'),
#     "pets" : None,
#     "cars" : [
#         {'model' : "BMW" , 'mpg' : 27.54},
#         {'model' : "Ferrari" , 'mpg' : 25.95}
#     ]
# }

# print(json.dumps(x))

# FORMAT RESULT :
    # The example above prints the json string , but it is not very easy to read , with no indentations
# and line breaks 
    # The json.dumps method has parameter to make it easier to read the result 

# import json

# x = {
#     "name" : "John",
#     "age" : 20,
#     "married" : True,
#     "divorced" : False,
#     "children" : ('Aun' , 'Killey'),
#     "pets" : None,
#     "cars" : [
#         {'model' : "BMW" , 'mpg' : 27.54},
#         {'model' : "Ferrari" , 'mpg' : 25.95}
#     ]
# }


# print(json.dumps(x, indent=4))

    # We can also define the separators , default value is (",",":") , which means using a comma and a
# space to separate each object , and a colon and a space to separate key from values  

# print(json.dumps(x , indent=4 , separators=(". ", "= ")))

# ORDER THE RESULT :
    # The json.dumps() method has a parameter to order the keys in the result

# import json

# x = {
#     "name" : "John",
#     "age" : 20,
#     "married" : True,
#     "divorced" : False,
#     "children" : ('Aun' , 'Killey'),
#     "pets" : None,
#     "cars" : [
#         {'model' : "BMW" , 'mpg' : 27.54},
#         {'model' : "Ferrari" , 'mpg' : 25.95}
#     ]
# }

# print(json.dumps(x , indent=4 , sort_keys=True))



