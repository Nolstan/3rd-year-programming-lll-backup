# Creating a class
# declaring a class named student
class student:
    # declaring a constructor
    def __init__(self):# in python self is mandatory
        self.fname = 'Nolstan' 
        self.lname = 'Logic'
    

    # what the init function does is that it initializes the attributes of the class 
    # when an object is created. In this case, it initializes the fname and lname 
    # attributes with the values 'Nolstan' and 'Logic' respectively.
    
student1 = student() # creating an object of the class student
print(student1.fname)