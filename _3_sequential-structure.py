# # characteristics of sequential structures
# # 1. They are executed in a specific order
# # 2. They are executed line by line
#
#
# # strings
# # characteristics of strings
# # 1.strings are immutable - cannot be changed after creation
# # 2.strings are ordered - each character has a specific index
#
# # text = "Hello, World!"
#
# # reversing a string
# # reversed_text = text[::-1]
# # print(reversed_text)
#
# # using a range loop to iterate through a string
# # for i in range(len(text)):
#     # print(text[i])
#
# # TUPLES
# # characteristics of tuples
# # 1. Tuples are immutable - cannot be changed after creation
# # 2.are subscriptable - can access elements using indexing
#
# # example of a tuple
# # # my_tuple = (1, 2, 3, 4, 5)
#
# # for item in my_tuple:
# #     print(item)
# # print(f'min {min(my_tuple)}')
# # print(f'max {max(my_tuple)}')
#
#
# # Tuple and packing means assigning multiple values to a single variable
# point = (10, 20)  # packing
# x, y = point  # unpacking
#
# # Tuples are not limited to data types
# data = (1, "Nolstan", 3.14, True)
# for item in data:
#     # print(item,end="," )
#
#
# # USE CASES OF TUPLES
# # 1. Storing multiple related values
# # 2. Returning multiple values from a function
#
#
# # a python code to calculate average of number in a list
# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# count = len(numbers)
# average = total / count
# # print(f'Average: {average}')
#
#
#
#
#
#
#
#
# # LISTS
# # characteristics of lists
# # 1. Lists are mutable - can be changed after creation
# # 2. Lists are ordered - each element has a specific index
#
# # example of a list
# a = [1, 2, 3, 4, 5]
# # # OR
# b = list((1, 2, 3, 4, 5))
# #
# # # print(b[-1]) # accessing the last element
# #
# #

# # # Methods of lists
# a.append(6)  # adds an element to the end of the list
# print(a)
# a.insert(3, 10)  # adds an element 10 at index 3 
# print(a)
# a.remove(3)  # removes an element from the list
# print(a)
# a.pop()  # removes the last element from the list
# print(a)
# a.clear()  # removes all elements from the list
# print(a)
# a.sort()  # sorts the list in ascending order
# print(a)
# a.reverse()  # reverses the order of the list
# print(a)
# a.count() #count the number of item occurence
# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# count = len(numbers)
# average = total / count
# print(f'Average: {average}')

# # a prigram to find  median CHATGPT ,A <DONT UNDERSTAND>
# numbers.sort()
# n = len(numbers)
# if n % 2 == 0:
#     median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
# else:
#     median = numbers[n // 2]
# print(f'Median: {median}')


# THIS ONE IS BETTER THAN THE ABOVE METHOD
# to find median

# import statistics as st

# _list = [12,23,12,45,56]

# median = st.median(_list)
# print(median)



# MULTI-DIMENSIONAL LISTS -> A LIST WITHIN A LIST

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
# print(matrix)

# Accessing elements in a multi-dimensional list
# print(matrix[1])  # Output: list 2

# access 5
# print(matrix[1][1])

# selecting portion from a list
# print(matrix[1:3])

# print(matrix[1][1:3]) #output [5,6]

# looping through a multi-dimensional list
# each and every element is a list

for row in matrix:
     for item in row:
         print(item)


# TODO : List addition

