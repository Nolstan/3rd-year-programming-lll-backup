
class circle:
    PI = 3.141592653589793
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2
    

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width 