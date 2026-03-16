
# A class variable is a variable that is shared among all instances of a class.
#  It is defined within the class but outside of any instance methods. 
# Class variables are used to store data

class circle:
    pi = 3.14 # class variable
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return circle.pi * self.radius ** 2
    

circle1 = circle(5)
print(circle1.calculate_area()) # this will use the class variable pi to calculate the area of circle1
  
import math
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    def calculate_diagonal_length(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)

rectangle1 = rectangle(10, 5)

print(rectangle.calculate_diagonal_length)