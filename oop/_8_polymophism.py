# polymophism is when a class can take many forms. 
# It is the ability of an object to take on many forms.
# It is the ability of a class to be used as a base class for other classes.

# its implemted thorugh method overriding and overloading

# method overriding is when a subclass provides a specific 
# implementation of a method that is already provided by its parent class.

class shape:
    def __init__(self,name):
        self.name = name
    def draw(self):
        print(f'{self.name} is being drawn')
    def draw(self,color):
        print(f'{self.name} is being drawn in {color}')
class _2D_shape(shape):
    def __init__(self,name,sides = 0):
        super().__init__(name) # this will call the constructor of the parent class
        # what the super function does is that it allows us to call the constructor
        #  of the parent class and pass the name parameter
        #  to it so that we can access it in the child class
        self.sides = sides
    def print_details(self):
        print(f'{self.name} has {self.sides} sides')


shape1 = _2D_shape('triangle',3)
print(shape1.name)
shape1.print_details()

shape2 = shape('circle')
shape2.draw('red')