import random
import sys

answer = random.randint(1, 10)

while True:
    try:
        guess = int(input("Choose a number (1-10): "))
        if 0 < guess < 11:
            if guess == answer:
                print('Correct!')
                break
        else:
            print('Hey! I said 1~10!')
    except ValueError:
        print('Please enter a number')
        continue







