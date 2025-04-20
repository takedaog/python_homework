class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating.")

    def sleep(self):
        print(self.name + " is sleeping.")


class Cow(Animal):
    def moo(self):
        print(self.name + " says Moo!")


class Chicken(Animal):
    def cluck(self):
        print(self.name + " says Cluck!")


class Pig(Animal):
    def oink(self):
        print(self.name + " says Oink!")


# Testing
cow = Cow("Betsy")
cow.eat()
cow.moo()

chicken = Chicken("Henrietta")
chicken.sleep()
chicken.cluck()

pig = Pig("Porky")
pig.eat()
pig.oink()