#LIST
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

#LIST SLICING 

amazon_cart = [
  'notebooks', 
  'sunglasses'
  'toys',
  'grapes'
]

print(amazon_cart[0:3:1])

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)


#MATRIX 

matrix = [
  [1,2,3],
  [2,4,6],
  [7,8,9]
]

print(matrix[0][1])

#LIST METHODS 

basket = [1,2,3,4,5]

#ADDING

basket.append(100)
print(basket)
basket.insert(4, 200)
print(basket)
basket.extend([101, 102])
print(basket)

#REMOVING

basket.pop
print(basket)
basket.pop(0)
print(basket)
basket.remove(4)
print(basket)

new_list = basket.pop(3)
print(new_list)

basket.clear()
print(basket)

basket2 = ['a','b','c','d','e']

print(basket2.index('d', 0, 4))

print('x' in basket2)
print('i' in 'Hi')
print(basket2.count('d'))
basket2.sort()
print(basket2)
print(sorted(basket2))
#Sorted does not modify
new_basked = basket.copy()
print(new_basket)
basket2.reverse()
print(basket2)

#LIST PATTERN

print(len(basket2))
print(basket2[::-1])
print(basket2)

print(list(range(1,101)))

new_sentence = ' '.join(['Hi', 'My', 'name', 'is', 'Jojo'])

print(new_sentence)

#LIST UNPACKING 

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)