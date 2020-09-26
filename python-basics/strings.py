#STRINGS

'Hi! Hello There'
"LOL"
print(type('Hi'))
username = 'supercoder'
password = 'supersecret'

long_string = '''
WOW
0 0
___
'''

print(long_string)

first_name = 'Patricia'
last_name = 'Faria'
full_name = first_name + ' ' + last_name
print(full_name)

#STRING CONCATENATION

print('Hello' + ' Lolly')

#TYPE CONVERSION

print(type(str(100)))
print(type(int(str(100))))

#ESCAPE SEQUENCE

weather = '\t It\'s "kind of" sunny \n Hope you have a good day!'

print(weather)
#\t => add a tab 
#\n => new line 

#FORMATTED STRINGS

name = 'Johnny'
age = 55

print(f'Hi {name}. You are {age} years old.')

print('Hi {}. You are {} years old.'.format('Johnny', '55'))

print('Hi {}. You are {} years old.'.format(name, age))

print('Hi {1}. You are {0} years old.'.format(name, age))

print('Hi {new_name}. You are {age} years old.'.format(new_name = 'Sally', age=100))

#STRING INDEXES

selfish = '01234567'
        #  01234567

# [start:stop:stepover]
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
print(selfish[-1])
print(selfish[::-1])

#IMMUTABILITY

#String Object does not support item assignment
#selfish[0] = '8' -> ERROR

selfish = '8'
#Works if complete change the value 

#LENGTH

greet = 'Hellooo'
print(len(greet))

#STRING METHODS

quote = 'to be or not to be'

print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'me'))
print(quote)

quote2 = quote.replace('be', 'me')
print(quote2)
