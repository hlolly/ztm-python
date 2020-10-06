class User():
    def sign_in(self):
        print('Logged In')

    def attack(self):
        print('Attack')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Lolly', 50)
archer1 = Archer('Chris', 105)

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()