#SET
#unordered collection of unique items

my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2)

print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list))

print(1 in my_set)
print(len(my_set))
print(list(my_set))

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

myset = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(myset.difference(your_set))
print(myset)

myset.difference_update(your_set)
print(myset)

print(myset.intersection(your_set))
print(myset & your_set)

print(myset.isdisjoint(your_set))

print(myset.issubset(your_set))

print(myset.issuperset(your_set))

print(myset.union(your_set))
print(myset | your_set)

myset.discard(5)
print(myset)