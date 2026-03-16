# encapsulation is data abstraction

# A field can be creadet with or withiout underscores

# with one undescore a field is protected
# with 2 underscores the field is private

class car:
    def __init__(self,name,color):
        self.__name = name # this will not display the cars name nor color for the variable is now protected
        self.__color = color

    def print_details(self):
        print(f'{self.__name} and its  {self.__color}')

car1 = car('Toyota','red')
# print(car1.__name) # this will provide an error because the variable is protected
# print(car1.__color) # same here

car1.print_details()