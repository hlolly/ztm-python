#LOOPS

for letter in 'Zero to Mastery':
  print(letter)
  print(letter)
  print(letter)

for item in (1,2,3,4,5):
  for x in ['a', 'b', 'c']
  print(item, x)

#ITERABLE - list, dictionary, tuple, set, string 
#ITERATED -> one by one check each item in the collection

user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for item in user.items():
  key, value = item;
    print(key, value)

for key, value in user.items():
    print(key, value)

#RANGE

print(range(100))

for number in range(0,100):
  print(number)

for _ in range(0, 10, 2):
  print(_)

for x in (10, 0, -1):
  print(x)

for y in range(2):
  print(list(range(10)))

#ENUMERATE 

for i,char in enumerate('Helloo'):
  print(i, char)

for i,top in enumerate((1,2,3)):
  print(i, top)

for i,numb in enumerate(list(range(100))):
  if numb == 50:
    print(f'index of 50 is: {i}')

# WHILE LOOP 

#INFINITE LOOP 

i = 0
while i < 50:
  print(i)

i = 0
while i < 50:
  print(i)
  break

i = 0
while i < 50:
  print(i)
  i += 1
else:
  print('Done with all the work')

i = 0
while i < len([1,2,3]):
  print(i)
  i += 1

while True:
  response = input('Say something: ')
  if (response == 'Bye')
  break

#CONTINUE 

my_list = [1,2,3]
for item in my_list:
  print(item)
  continue

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
  continue

#PASS

my_list = [1,2,3]
for item in my_list:
  #Thinking about it
  pass

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
  pass



