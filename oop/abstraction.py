# Private - Put _ to say that it shouldn't change
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('Run')

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old')


player1 = PlayerCharacter('Lolly', 205)
player1.speak()