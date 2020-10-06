class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged In')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


wizard1 = Wizard('Lolly', 50, 'lolly@gmail.com')

print(wizard1.email)

#INTROSPECTION

print(dir(wizard1))