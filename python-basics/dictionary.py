#Dictionary

dictionary = {
  'weapons': [1,2,3],
  'greeting': 'hello',
  'is_Magic': True,
  123: [1,2,3],
  True: 'Hi'
}

my_list = [{
  'a': [1,2,3],
  'b': 'hello',
  'x': True
  },
  'a': [4,5,6],
  'b': 'bye',
  'x': False
  }
  ]

print(dictionary['weapons'][1])
print(dictionary(True))
print(my_list[0]['a'][2])

#DICTIONARY HOLD MORE INFORMATION AND DOES NOT HAS AN ORDER

#DICTIONARY METHODS

user = {
  'basket': [1,2,3],
  'greet': 'Hello',
  'age': 20,
  'color': 'Blue',
  'is_Male': False
}

print(user['basket'])
print(user.get('size'))
print(user.get('age', 55))

user2 = dict(name='John')
print(user2)

print('basket' in user.keys())
print('hello' in user.values())
print(user.items())

print(user.update({'age': 55}))
print(user)

print(user.pop('age'))
print(user)

print(user.popitem())
print(user)

user2 = user.copy()
print(user2)

user.clear()
print(user)
print(user2)