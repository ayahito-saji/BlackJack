from Person import *

class Player(Person):
    def __init__(self, name, coin):
        super().__init__(name)
        self.coin = coin