class Animal:
    animal_dict = {}
    food={}
    noise={}

    def __init__(self, animal_name):
        self.animal_name = animal_name
        self.count=0
    def take_count(self):
        self.count = int(input("Enter count of {}'s".format(self.animal_name)))
    def take_input(self):
        self.temp_food = {}
        self.temp_animal_dict = {}
        self.temp_noise= {}
        for i in range(1, self.count + 1):
            self.name = input("Enter the name of {} {}: ".format(self.animal_name, i))
            self.category = input("Enter the Catogory of {} {}: ".format(self.animal_name, i))
            self.sound = input("Enter Noise made by {} {}: ".format(self.animal_name, i))
            self.feed = input("Enter food loved by {} {}: ".format(self.animal_name, i))
            self.temp_animal_dict[self.name] = self.category
            self.temp_food[self.name] = self.feed
            self.temp_noise[self.name] = self.sound
            self.animal_dict.update(self.temp_animal_dict)
            self.food.update(self.temp_food)
            self.noise.update(self.temp_noise)


class Lion(Animal):
    def __init__(self):
        super().__init__("Lion")
class Tiger(Animal):
    def __init__(self):
        super().__init__("Tiger")
class Giraffe(Animal):
    def __init__(self):
        super().__init__("Giraffe")
class Elephant(Animal):
    def __init__(self):
        super().__init__("Elephant")
class Deer(Animal):
    def __init__(self):
        super().__init__("Deer")

l = Lion()
l.take_count()
l.take_input()
t = Tiger()
t.take_count()
t.take_input()
g = Giraffe()
g.take_count()
g.take_input()
e = Elephant()
e.take_count()
e.take_input()
d = Deer()
d.take_count()
d.take_input()
print("Zoo Animals Dictionary: {}".format(Animal.animal_dict))
print("Food: ")
print(*[str(k) + ':' + str(v) for k,v in Animal.food.items()], sep="\n")
print("Noise: ")
print(*[str(k) + ':' + str(v) for k,v in Animal.noise.items()], sep="\n")

