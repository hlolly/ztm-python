# FUNCTION

#PARAMETERS (NAME)

def say_hello(name,emoji):
  print(f'Hello {name} {emoji}')

#ARGUMENTS (PATRICIA)
say_hello('Patricia', ':)')

# KEYWORD ARGUMENTS

say_hello(emoji=':)', name='Patricia')

# DEFAULT PARAMENTERS

def say_hello(name='Darth Vader', emoji='>:('):
  print(f'Hello {name} {emoji}')

say_hello()

# RETURN

def sum(num1, num2):
  return num1 + num2

total = sum(10,5)
print(sum(10,total))

def sum(num1, num2):
  def another_func(n1, n2):
    return n1 + n2
  return another_func(num1, num2)

total = sum(10,20)
print(sum(total))

def test(a):
  '''
  Info: this function tests and prints param a
  '''
  print(a)

test('!!!')

help(test)

print(test.__doc__)

# *args **kwargs

def super_func(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

#Rule: params, *args, default parameters, **kwargs
#(name, *args, i='hi', **kwargs)

# SCOPE - what variables do I have access to?

a = 1

def parent():
  a = 10
  def confusion():
    return sum
  return confusion()

print(parent())
print(a)

# 1 - start with locals
# 2 - parent local
# 3 - global
# 4 - built-in python functions

total = 0

def count():
  global total 
  total += 1
  return total

print(count())

def count(total):
  total += 1
  return total

print(count(count(count(total))))

# NON LOCAL 

def outer():
  x = "local"
  def inner():
    nonlocal x
    x = "nonlocal"
    print("inner:", x)

  inner()
  print("outer:", x)

outer()
 