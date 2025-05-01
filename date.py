# PYTHON DATE : 
    # A python date is not a datatype of its own , but we can import a module named datetime to work
# with dates as date objects .

# import datetime

# x = datetime.datetime.now()

# print(x)

# DATE OUTPUT :
    # When we execute the code from the example above the following result will be

# 2025-05-01 16:07:41.966789

# The date contains , year,month,day ,hour,minute,second and microsecond

# The datetime module has many method to return information about them later in this chapter

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime('%A'))

# CREATING DATE OBJECTS :
    # To create a date , we can use datetime() class (constructor) of the datetime module 
    # The datetime() class requires 3 parameters to create a date : year , month , day

# import datetime

# x = datetime.datetime(2025 , 2 , 1)
# print(x)

    # The datetime class also takes parameter for time and timezone (hour , minute , second microsecond,
# tzone) , but they are optional , and has a default value of 0 , (None for Timezone)

# THE strftime METHOD :
    # The datetime object has a method for formatting date objects into readable strings 
    # The mthod is called strftime() , and takes 1 parameter , format , to specify the formt of the 
# returned string 


# import datetime

# x = datetime.datetime(2025 , 5 , 1)

# print(x.strftime('%B'))










