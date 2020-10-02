from functools import reduce

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))


# MAP

my_list = [1,2,3]

def multiply(item):
    return item*2

print(list(map(multiply, my_list)))


# FILTER

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))

# ZIP

your_list = [10,20,30]
their_list = (5,4,3)

print(list(zip(my_list, your_list, their_list)))

# REDUCE

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 10))
print(my_list)

# LAMBDA EXPRESSIONS - Functions used only once

print(list(map(lambda item: item**2, their_list)))

a = [(0,2),(4,3),(9,9),(10,-1)]

a.sort(key=lambda x: x[1])
print(a)