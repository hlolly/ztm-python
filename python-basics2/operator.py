is_magician = False
is_expert = True

if is_magician and is_expert:
  print("You are a Master Magician")

elif is_magician and not is_expert:
  print("At least you are getting there")

elif not is_magician:
  print("You need magic powers")

print(True == 1)
print('1' == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print(True is 1)
print('1' is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])