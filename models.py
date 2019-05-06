class Dragon:
    def __init__(self):
        self.defense = 600
        self.damage = 600

    def replenish(self):
        self.defense = 600
        self.damage = 600

class Soldier:
    def __init__(self):
        self.defense = 2
        self.damage = 2

    def replenish(self):
        self.defense = 2
        self.damage = 2

class WhiteLord:
    def __init__(self):
        self.defense = 100
        self.damage = 50

    def replenish(self):
        self.defense = 100
        self.damage = 50

class Walker:
    def __init__(self):
        self.defense = 3
        self.damage = 1

    def replenish(self):
        self.defense = 3
        self.damage = 1
def main():
    print("hello world")


if __name__ == "__main__":
    main()