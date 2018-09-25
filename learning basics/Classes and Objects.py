class Enemy:

    def __init__(self, x):
        print("I'm the beast!!!!!")
        self.life = x


    def attack(self):
        if self.life > 0:
            self.life -= 25
            if self.life > 0:
                print("Laude Lag Gaye!")
            else:
                print("AAAAAAAAHHHHHHHHHHH")
        else:
            print("The DEAD cannot be KILLED!!!")




    def checklife(self):
        if self.life > 0:
            print("Abhi Jinda hu: Life =", self.life)
        else:
            print("Marr gaya sala!")

class Baap(Enemy):

    def __init__(self, x):
        print("BAAP HU BANCHO")
        self.life = 999999999999


Chuchi = Baap(75)

Chuchi.attack()
Chuchi.checklife()
Chuchi.attack()
Chuchi.attack()
Chuchi.attack()
Chuchi.checklife()
