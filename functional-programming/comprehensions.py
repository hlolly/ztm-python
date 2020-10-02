# LIST COMPREHENSION

my_list = [char for char in 'Hello']
my_list2 = [num for num in range(0,10)]
my_list3 = [num**2 for num in range(0,10)]
my_list4 = [num**2 for num in range(0,10) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# SET COMPREHENSION

my_set = {char for char in 'Hello'}
my_set2 = {num for num in range(0,10)}
my_set3 = {num**2 for num in range(0,10)}
my_set4 = {num**2 for num in range(0,10) if num % 2 == 0}

print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)

# DICTIONARY COMPREHENSION

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict2)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([v for v in some_list if some_list.count(v) > 1]))


print(duplicates)