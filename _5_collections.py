# SET - is a collection of unique elements
# SETS are unordered, unindexed, and cannot be accessed using index
# A set is mutable, meaning you can add or remove elements from it

# ARE SETS SUBSCRIPTABLE?
# sets are not subscriptable because they are unordered
# creating a set
my_set = {1, 2, 3, 4,4, 5}
print(my_set)


# SET METHODS
# add()
my_set.add(6) # adds an element to the set
# clear()
my_set.clear() # removes all elements from the set
# copy()
my_set.copy() # returns a copy of the set
# difference()
my_set.difference({1, 2, 3})# returns a set that contains the difference between two sets
# difference_update()
my_set.difference_update({1, 2, 3})# removes the elements in the set that are also in another set
# discard()
my_set.discard(4)
# intersection()
my_set.intersection({1, 2, 3})
# intersection_update()
my_set.intersection_update({1, 2, 3})
# isdisjoint()
# issubset()
# issuperset()
# pop()
# remove()
# symmetric_difference()
# symmetric_difference_update()
# union()
# update()



# REMOVING DUPLICATE?
# Just use a set