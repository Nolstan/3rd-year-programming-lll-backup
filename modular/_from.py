from mathpackage.geom import  circle
nums = [1, 2, 3, 4, 5]
# print(f"Minimum = { min_(nums)}")
# print(f"Maximum = { max_(nums)}")
print(f"Area of circle with radius 5 is {circle(5).area():.2f}")


# To get the documentation of a module or a function in a module we can use the help() function

# print(min_.__doc__)


# A package is a collection of modules that are organized in a directory hierarchy. 
# It is a way to organize related modules together. A package can contain subpackages and modules.



# WHY IS USING FROM BETTER THAN IMPORTING THE WHOLE MODULE?
# It is better to use from because it allows us to import only the specific
# functions or classes that we need from a module, which can save memory and improve performance.