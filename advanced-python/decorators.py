def hello():
    print('Hello');

greet = hello
del hello

print(greet())

# Higher Order Function HOC

def run(func):
    func()

def run2():
    def func():
        return 5
    return func

def still():
    print('Still Here')

a = run(still)

print(a)

# DECORATOR

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func

@my_decorator
def hi(greeting, emoji=':)'):
    print(greeting, emoji)

hi('Hi')

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i*5

long_time()
long_time2()

