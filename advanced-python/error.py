# ERROR HANDLING

while True:
    try:
        age = int(input('What is your age? '))
        10/age
        #raise Exception('Hey, cut it out')
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter a age higher than 0')
    else:
        print('Thank you')
        break
    finally:
        print('Ok, I am finally done')

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum('1', 2))