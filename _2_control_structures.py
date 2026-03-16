# if ...else statement
# for loop
# while loop

# age = 200

# if age >= 18 and age <= 99:
#     print("You are an adult.")
# elif age >= 100:
#     print('You must be dead by now bro')
# else:
#     print('You son of a bitch you are still a child')


# grade = "E"

# if grade == "A":
#     print("Bright azz nigga")
# elif grade == "B":
#     print("Yall can do better than this")
# elif grade == "C":
#     print("Lucky bastard")
# elif grade == "D":
#     print("watch out next time u might hit the bottom")
# elif grade == "E":
#     print("dead meat")
# else:
#     print("You chose the wrong program")

# for loop

# for i in range(0,5):
    # print(i)
    
# controlling range
# for i in range(1,10):
    # print(i)# Output: 1 2 3 4 5 6 7 8 9



# for i in range(1,10,2):# 1 is start point ,10 is the end point and 2 is the step
#     print(i,end=" ")

# Implement a program that displays
# Multiplication table based
# on the value from a user

# number = int(input("Enter a number: "))

# for i in range(1,11):
    # pass
    # print(f"{number} x {i} = {number * i}")



# write a program that loops numvers from 0 to 100
#  fizz when the numbe is even
# fuzz when the number is divisible by 7
# when the numbe is divisible by 15 print hooray

# for i in range(101):
#     if i % 15 == 0:
#         print("Hooray")
#     elif i % 7 == 0:
#         print("Fuzz")
#     elif i % 2 == 0:
#         print("Fizz")
#     else:
#         print(i)

# TODO: match...case
# its more like switch...case in other languages
grade = "A" or "a"
match grade:
    case "A":
        print("Bright azz nigga")
    case "B":
        print("Yall can do better than this")
    case "C":
        print("Lucky bastard")
    case "D":
        print("watch out next time u might hit the bottom")
    case "E":
        print("dead meat")
    case _:
        print("You chose the wrong program")