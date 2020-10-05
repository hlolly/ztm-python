from utility import multiply, divide
from shopping.more_shopping import shopping_cart
import random
import sys

if __name__ == '__main__':
    print(shopping_cart.buy('Apple'))
    print(multiply(2,3))
    print(max([1,2,3]))

#help(random)
#print(dir(random))

print(random.random())
print(random.randint(1, 10))
print(random.choice([1,2,3,4,5]))

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

print(sys)

sys.argv
# TERMINAL - WATCH AGAIN