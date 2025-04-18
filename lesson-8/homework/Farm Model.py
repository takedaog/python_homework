class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Dog", age)

    def fetch(self):
        print(f"{self.name} is fetching the ball!")


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cow", age)

    def milk(self):
        print(f"{self.name} is being milked.")


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Chicken", age)

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")


# Example usage:
dog = Dog("Rex", 5)
cow = Cow("Bessie", 4)
chicken = Chicken("Clara", 2)

dog.make_sound()
dog.fetch()

cow.make_sound()
cow.milk()

chicken.make_sound()
chicken.lay_eggs()
