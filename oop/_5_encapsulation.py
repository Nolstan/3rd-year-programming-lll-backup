# encapsulation is data abstraction

# A field can be creadet with or withiout underscores

# with one undescore a field is protected and it can be accessed within the class and its subclasses but not outside the class.
# with 2 underscores the field is private and it cannot be accessed outside the class. It can only be accessed within the class itself.

class car:
    def __init__(self,name,color):
        self._name = name # this will not display the cars name nor color for the variable is now protected
        self._color = color

    def print_details(self):
        print(f'{self._name} and its  {self._color}')

car1 = car('Toyota','red')
# print(car1.__name) # this will provide an error because the variable is protected
# print(car1.__color) # same here

car1.print_details()