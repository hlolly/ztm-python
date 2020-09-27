#CONDITIONAL LOGIC

is_old = True
is_licenced = True

if is_old and is_licenced:
  print('You are old enough to drive and you have a licence!')

#elif is_licenced:
  print('You can drive now!')

else:
  print('You are not of age!')

#TRUTHY AND FALSY

password = '123'
username = 'johnny'

if password and username:
  print('Hi')

# TERNARY OPERATOR 

# condition_if_true if condition else condition_if_false

is_friend = True
can_message = "Message Allowed" if is_friend else "Not Allowed"

print(can_message)

# SHORT CIRCUITING 

is_Friend = True
is_User = True

if is_Friend or is_User:
  print('Best Friends Forever')

# LOGICAL OPERATOR

print(4 > 5)
print(4 < 5)
print(4 == 5)
print('a' > 'A')
print(1 < 2 > 3 < 4)
print(4 >= 5)
print(4 <= 5)
print(4 != 5)
print(not(True))

# Methods vs Fuctions

# list()
# print()
# max()
# min()
# input()

def some_random_stuff():
  pass

some_random_stuff() 

'Hello'.capitalize() 

#CLEAN CODE 

def is_even(num):
  return num % 2 == 0

print(is_even(51))

