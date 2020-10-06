class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Lolita', 3)
cat2 = Cat('Zelda', 2)
cat3 = Cat('Luigi', 5)


def get_oldest(*args):
    return max(args)

print(f"The oldest cat is {get_oldest(cat1.age, cat2.age, cat3.age)} years old")

