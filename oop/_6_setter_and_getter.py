
# getters and setters are used to access and modify the private attributes of a class. 
# They are also used to provide a way to validate the data before it is set to the private attributes.
class car:
    def __init__(self,name,color):
        self.__name = name # this will not display the cars name nor color for the variable is now protected
        self.__color = color

    def print_details(self):
        print(f'{self.__name} and its  {self.__color}')

    def set_name(self,name):
        self.__name = name
    def set_color(self,color):
        self.__name = color

car1 = car('Toyota','red')
# print(car1.__name) # this will provide an error because the variable is protected
# print(car1.__color) # same here

car1.print_details()
car1.set_name('Honda') # this will change the name of the car to Honda
car1.set_color('blue') # this will change the color of the car to blue
car1.print_details()