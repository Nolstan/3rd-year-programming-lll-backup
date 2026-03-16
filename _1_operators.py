# OPERATOrs

# assignment operator
# comparison operator
# Logical operator
# identity operator
# membership operator

# 1 Assignent - what it does is to assign a value to a variable
# eg x = 5
#  2 Comparison - what it does is to compare two values and return a boolean value
# eg x == 5

# a,b ,c = 5, 10, 15
# print(a < b)  # Output: True

# posible for strings too

# a,b,c = "Hello", "World", "Python"
# print(a < b)  # Output: True


# can we use < > on strings?
# print(b > c)  # Output: True
# HOW IS IT COMPARING STRINGS EXACTLY?
# It uses Alphabetical order to compare strings specifically ASCII values of characters


# 3 Logical - what it does is to combine multiple boolean values and return a single boolean value
# eg x > 5 and x < 10

# a , b = 7, 12

# print(a > 5 and b < 15)  # Output: True
# print(a > 10 or b < 15)  # Output: True

# 4 Identity - what it does is to compare the memory location of two objects and return a boolean value
# eg x is y

# 5 Membership - what it does is to check if a value is present in a sequence and return a boolean value
# eg x in y

# the power operator is used to raise a number to a certain power

# a = 2 
# b = 3

# print(a ** b)  # Output: 8


# # the floor division operator is used to divide two numbers and return the largest integer less than or equal to the result
# c = 7
# d = 3
# print(c // d)  # Output: 2


# A program that has a username and password  in variables
# and asks the user to input their username and password
# Compares the input with the stored username and password

# stored_username = "Nolstan"
# stored_password = "password"
# input_username = input("Enter your username: ")
# input_password = input("Enter your password: ")
# if input_username == stored_username and input_password == stored_password:
#     print("Login successful!")
# else:
#     print("Login failed! Incorrect username or password.")

# identity operator is and is not example
a = 4
b = a

print(a is b)  # Output: True

# what is happening here is that both a and b are pointing to the same memory location


for i in range(101):
    if i % 15 == 0:
        print(f"number is {i} so its  Hooray")
    elif i % 7 == 0:
        print(f"number is {i} so its  Fuzz")
    elif i % 2 == 0:
        print(f"number is {i} so its Fizz")
    else:
        print(i)