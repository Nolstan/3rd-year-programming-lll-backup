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

# Python compares strings lexicographically by checking characters from left to right 
# and comparing their Unicode (ASCII) values. The comparison stops when a different character is found





# 3 Logical - what it does is to combine multiple boolean values and return a single boolean value
# eg x > 5 and x < 10

# a , b = 7, 12

# print(a > 5 and b < 15)  # Output: True
# print(a > 10 or b < 15)  # Output: True

# 4 Identity - what it does is to compare the memory location of two objects and return a boolean value
# eg 
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)      # True
# print(a is c)      # False
# print(a == c)      # True

# 5 Membership - what it does is to check if a value is present in a sequence and return a boolean value
# eg x in y
# print("H" in "Hello")  # Output: True


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
a = 400000
b = a
c = int("400000") # forcing python to create a new object in memory

print(a is b)  # Output: True
print(a is c)  # Output: True
# Python caches  integers  to save memory and speed up programs.
# thats why a and c are pointing to the same memory location because 
# they are both 4 which is a small integer that is cached by Python



for i in range(101):
    if i % 15 == 0:
        print(f"number is {i} so its  Hooray")
    elif i % 7 == 0:
        print(f"number is {i} so its  Fuzz")
    elif i % 2 == 0:
        print(f"number is {i} so its Fizz")
    else:
        print(i)

        matrix = [[5,8,2], [6,3,7],[4,1,9]]
        diagonal = [matrix[i][i] for i in range(len(matrix))]
        print(diagonal)

        x = 10 
        def change():
            x = x + 5
            return
        change()
        print(x)