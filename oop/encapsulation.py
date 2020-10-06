class PlayerCharacter:
    #Class Object Attribute
    membership = True
    def __init__(self, name='Annonymous', age=0):
        #if (age > 18):
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Lolly', 32)
player2 = PlayerCharacter('Chris', 34)
player2.attack = 50
player3 = PlayerCharacter.adding_things(2,3)

print(player1.name)
print(player2.age)
print(player2.attack)
print(player1.shout())
print(player1.membership)
print(player3.age)
