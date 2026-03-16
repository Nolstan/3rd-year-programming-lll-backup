class student:
    # declaring a constructor
    def __init__(self, fname, lname):# in python self is mandatory
        self.fname = fname 
        self.lname = lname
    def print_details(self):
        print(f'Hello {self.fname} {self.lname}')
student1 = student('Nolstan', 'Logic') # creating an object of the class student
print(student1.print_details())
student2 = student('Mick','Mickelar')
# print(student2.fname)