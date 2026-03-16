# A function is a block of code which only runs when it is called.
#  You can pass data, known as parameters, into a function.
#  A function can return data as a result.

# def greet():
#     print('hello Nolstan')

# def greet(name):
#     print(f'hello {name}')

# def  greet(fname, lname):
#     print(f'hello {fname} {lname}')

# greet("Nolstan", "logic" ) # calling the function    


# default values are used when we want to give a default value 
# to a parameter in case the user does not provide one
# def  greet(fname = 'User', lname ='Name'):
#     print(f'hello {fname} {lname}')

# greet()


# def  greet(fname = 'User', lname ='Name'):
#     print(f'hello {fname} {lname}')

# greet('Nolstan','Logic') # this will display Nolstan Logic


# # Mixing deault values with not complete parameters
# def greet(fname ,sname ='user'):
#     print(f'Hello {fname} {sname}')
# greet()# this will provide an error because there is no default value 

#  # Mixing deault values with not complete parameters
# def greet(fname ,sname ='user'):
#     print(f'Hello {fname} {sname}')
# greet('Nolstan') #this will work ,it will assign the name to fname and sname will use the default value

#  # Mixing deault values with not complete parameters
# def greet(fname ,sname ='user'):
#     print(f'Hello {fname} {sname}')
# greet('Nolstan' , sname = 'Logic')


# def fun1(a,b,c,d = 0):
#     print(a,b,c,d)

# fun1(1,2,3)


# def fun1(a,b,c,d = 0):
#     # print(a,b,c,d)

# # fun1(1,2,3) # Parameters with default value should be placed at the end

# def fun1(a,b,c,d = 0):
#     print(a ,b,c,d,sep='-')

# fun1(b = 70,a =23,c = 5,d =10)# order doesnt matter it will still assign values based on the argument name 




# def add(num1 ,num2):
#     total = num1 + num2
#     return total

# sum_ = add(1,3)
# print(f'Total = {sum_}')#or
# print(f'Total = {add(1,3)}')# and this is efficient
# # The third way to print this
# add(1,3)


nums = [1,2,3,4,5,5,6,7]
print(nums.pop())# use shift+tab to open the man like page for the functions

nums.extend([8,9,10])# this will add the elements to the end of the list
print(nums)


# variable argument and key arguments
# this is used when we want to pass a variable number of arguments to a function
# *args is used to pass a variable number of non-keyword arguments to a function
# **kwargs is used to pass a variable number of keyword arguments to a function


# def add(*args):
#     # print(args)
#     total = 0
#     for arg in args:
#         total = arg + total

#     return total
#     # return sum(args)

# add(1,2,3,4,5,6,7,8,8,8,23,3)
# notice args is not a keyword ,u can use any name but start with * to indicate that it is a variable argument

# assuming 
def add(*args,b):
    # print(args)
    total = 0
    for arg in args:
        total = arg + total

    return total
    # return sum(args)
# how are we going to assign value of b when we are passing variable number of arguments
# we can assign value of b by using keyword arguments like this
    
# add(1,2,3,4,5,6,7,8,8,8,23,3,b=100)

# kwargs is used to pass a variable number of keyword arguments to a function
# it returns a dictionary of the keyword arguments passed to the function

def printer(**kwargs):
    # print(kwargs)
    for key , value in kwargs.items():
        print(f'{key} : {value}')

# printer(name = 'Nolstan', age = 23, city = 'Tokyo')

#  return the maximum and minmum (multiple values)


# returning multiple values from a function is done by returning a tuple of the values
# def min_max(list_nums):
#     return max(list_nums) , min(list_nums)

# nums = [1,2,3,4,5,5,6,7]
# min_ , max_ = min_max(nums)
# print(f'Minimum = {min_} , Maximum = {max_}')



# lambda function is an anonymous function that 
# can take any number of arguments but can only have one expression
# it is used when we want to create a small function that can be used only once and
# we dont want to give it a name


# characteristics of lambda function
# 1. it is an anonymous function
# 2. it can take any number of arguments but can only have one expression
# 3. it is used when we want to create a small function that can be used only once 

# lambda arguments : expression 
hello = lambda : 'Hello World'
print(hello()) 
hello = lambda name : f'Hello {name}'
# print(hello('Nolstan'))


power = lambda num1 , num2 : num1 ** num2
print(power(2,3))


# NEXT TIME WILL DO OOP