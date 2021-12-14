class Common:
    def __init__(self):
        self.stay = 'House'

    def data(self):
        print("All are taking breathe")
    

class Human(Common):
    def __init__(self):
        self.human_sleep = 8
        super().__init__()

    def data(self):
        super().data()
        print("Human is self care person")

    def details(self):
        print(f"Human sleeping hours {self.human_sleep}")
        print(f"Humans stay in {self.stay}")


class Dog(Common):
    def __init__(self):
        super().__init__()
        self.dog_sleep = 4

    def data(self):
        super().data()
        print("Dog is pet animal")

    def details(self):
        print(f"Dog's sleep {self.dog_sleep}")
        print(f"Dog's stay in {self.stay}")


Arun = Common()

rohan = Arun

rohan.data()
