# using normal loop to find even numbers

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evn = []

for i in lists:
    if i % 2 == 0:
        evn.append(i)

print(evn)
# using comprehension

evn = [i for i in lists if i % 2 == 0]
print(evn)
 

 
squared =[i**2 for i in lists]
print(squared)