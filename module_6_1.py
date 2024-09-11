class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if issubclass(type(food), Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    
    def __init__(self, name):
        super().__init__(self)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


















"""
class MotorTransport(object):
    def __init__(self, color, year, auto_type):
        self.color = color
        self.year = year
        self.auto_type = auto_type

        # тормозить
    def stop(self):
        print("Pressing the brake pedal")

        # ехать
    def drive(self):
        print('WRRRRRUM!')


ferrari_testarossa = MotorTransport('Red', 1987, 'passenger car')

ferrari_testarossa.drive()
"""