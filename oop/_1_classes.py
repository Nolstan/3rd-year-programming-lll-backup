# Creating a class
# declaring a class named student
class student:
    # declaring a constructor
    def __init__(self):# in python self is mandatory
        self.fname = 'Nolstan' 
        self.lname = 'Logic'
student1 = student() # creating an object of the class student
print(student1.fname)