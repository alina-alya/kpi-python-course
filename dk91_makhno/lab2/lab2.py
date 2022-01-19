class Personage():
    def __init__(self, name, party, sex):
        self.name = name
        if sex is "man" or sex is "woman":
            self.sex = sex
        else:
            return "error: there can be no such sex"
        self.party = party

    def for_the(self):
        print("For the ", self.party)

class Mage(Personage):
    def __init__(self, name, party, sex, lvl):
        super().__init__(name, party, sex)
        if int(lvl):
            self.lvl = lvl
        else:
            return "error: Level must be a number!"

    def spell(self):
        if self.lvl <= 5 :
            print("puck!")
        elif self.lvl > 5 and self.lvl <= 10:
            print("bang!")
        elif self.lvl > 10:
            print("trah! babah!!!!")

class Warrior(Personage):
    def __init__(self, name, party, sex, item):
        super().__init__(name, party, sex)
        if item is "sword" or item is "bow":
            self.item = item
        else:
            return "item = sword or bow"

    def attack(self):
        if self.item is "sword" :
            print("hit!")
        elif self.item is "bow":
            print("shot!")




def main():
    h = Personage("bebra", "Horde", "man")
    h.for_the()
    war = Warrior("bebra", "Horde", "man", "sword")
    war.attack()
    mag = Mage("bebra", "Horde", "man", 25)
    mag.spell()


if __name__ == '__main__':
    main()


