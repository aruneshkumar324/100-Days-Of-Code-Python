from first import Human, Dog

class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("yes it can")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Fish also take breathe")

    def swim(self):
        print("Yes fish can swim")


animal = Animal()
# print(animal.eyes)
# animal.breathe()

fish = Fish()
# fish.swim()
# print(fish.eyes)
# fish.breathe()


def first_class():
    human = Human()
    human.details()
    human.data()

    dog = Dog()
    dog.details()
    dog.data()


# first_class()





















