#TUPLES
# *IMUTABLE LIST (UBER/LOCATIONS)

my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)
print(my_tuple.count())
print(my_tuple.index(5))
print(len(my_tuple))

new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,z, *other = (1,2,3,4,5)
print(z)