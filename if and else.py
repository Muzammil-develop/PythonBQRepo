# PYTHON CONDITION AND IF STATEMENT :
    # Python supports the usual logical condition from mathematics

# 1. Equals to =
# 2. Not Equals to !=
# 3. Greater than >
# 4 . less than <
# 5. Greater than Equals to >=
# 6. Less than Equals to <=

    # These conditions can be used in different ways most commonly in 'if statement' and 'loops'
    # An f statement is written by using 'if' keyword .

# a = 200
# b = 180
# if a > b:
#     print('A is greater value') 

    # In this example we use 2 variables , a and b , we give a value of 200 in A and 180 in b . As we
# know that 200 is greater than 180 so we print the statment "A is greater value"

# INDENTATION :
    # Python relies on indentation (whitspaces at the beginning of line) to define scope in 
# the code . Other pogramming languages often use curly-brackets for this purpose .

    # If statement without indentation will raise error .

# a = 200
# b = 180
# if a > b:
# print('A is greater')

# ELIF :
    # Elif condition in python says if the previous condition is not true then try this 

# a = 200
# b = 200
# if a > b:
#     print('A is greater')
# elif a == b:
#     print('A and b is Equal')

    # In this example A is Equal to b so first condition is not true , but the elif condition is true 
# so we print to screen that 'a and b are equal'

# ELSE :
    # The else keyword is catching averything that is not catched by preceding conditions .

# a = 200
# b = 170
# if a < b:
#     print('A is less than b')
# elif a == b:
#     print('A and b is same')
# else:
#     print('A is greater than b')

    # In this example A is less than b which is not true , also elif condition is not true , so we go 
# to the else condition and print to screen that 'a is greater than b'

    # We can also have an else without elif condition .

# a = 20
# b = 15
# if a < b :
#     print('A is less than b')
# else:
#     print('A is greater than b')

# SORT HAND IF :
    # If we want to execute 1 statement we can put it on the same line as the if statement .

# a = 20
# b = 10
# if a > b : print('A is greater than b')

# SHORT HAND IF / ELSE :
    # If we have only 1 statement to execute , 1 for if and 1 for else . we can put all in 
# same line . 

# a = 20
# b = 10
# print('A') if a > b else print('B')

    # This technique is known as Ternary Operator and Conditional Expression . 
    # We can also have multiple else statement on the same line . 

# a = 200
# b = 100
# print('A') if a > b else print('=') if a == b else print('b')

# AND :
    # The and keyword is a logical operator and is used to combine conditional statement .

# a = 200
# b = 150 
# c = 1000
# if a > b and c > a :
#     print('A and C is greater values')

# OR :
    # The or keyword is a logical operator and is used to combine conditional statement 

# a = 200
# b = 150
# c = 100
# if a > b and b > c :
#     print('Atleast 1 condition is True')

# NOT :
    # The not keyword is a logical operator .and is used to reverse the result of conditional 
# statement

# a = 100
# b = 200
# if not a > b:
#     print('A is not greater than b')

# NESTED IF :
    # We can have if statement inside if statement and this is called nested if statement

# a = 40
# if a > 20:
#     print('A is greater than 20')

#     if a > 30:
#         print('A is greater than 30')
#     else:
#         print('A is less than 30')

# THE PASS STATEMENT :
    # if statement can not be empty , but if we left empty for some reason , than we have to use
# pass satement to avoid error

# a = 200
# b = 100

# if a > b:
#     pass

# PYTHON MATCH :
    # The match statement is used to perform different statements based on different conditions .

    # Instead of wrwiting many if else condition we use mtch statement .
    # The match statements select one of many code blocks to be executed .

# SYNTAX :
    # match expression :
        # case x :
            # vode block
        # case y:
            # code block
        # case z:
            # code block

    # This is how it works          
        # 1. The match expression is evaluated once 
        # 2. The values of expression is compared with the values of each case . 
        # 3. if there is a match . the associated block of code is executed 
        
    # The example below uses the weekday number to print weekday name . 

# day = 4
# match day :
#     case 1:
#         print('Monday')
#     case 2 :
#         print('Tuesday')
#     case 3 :
#         print('Wednesday')
#     case 4 :
#         print('Thursday')
#     case 5:
#         print('Friday')
#     case 6 :
#         print('Saturday')
#     case 7 :
#         print ('Sunday')

# DEFAULT VAlUE :
    # use the '_' character as the last case value . if we want a code block to execute when there 
# are not other matches 

# day = 4
# match day:
#     case 6 :
#         print('Today is Saturday')
#     case 7 :
#         print('Today is Sunday')
#     case _ :
#         print('Looking forward to the weekend')

    # The value _ will always match , so it is important to place it as the last case to make it behave
# as a default case .

# COMBINE VALUES :
    # Use the pipe characters | as an operator in the case evaluation to check for more than 1 value
# match in 1 case .

# day = 4
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print('Today is week day')
#     case 6 | 7:
#         print('I love weekends')

# IF STATEMENTS AS GUARDS :
    # We can use if statement the the case evaluation as an extra-condition check .

# month = 5
# day = 4
# match day :
#     case 1 | 2 | 3 | 4 | 5 if month == 4:
#         print('A weekday in April')
#     case 1 | 2 | 3 | 4 | 5 if month == 5:
#         print('A weekday in May')
#     case _ :
#         print('No Match')    
    



    





