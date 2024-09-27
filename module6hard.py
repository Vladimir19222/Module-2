from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return [self.__color[0], self.__color[1], self.__color[2]]

    def __is_valid_color(self, r, g, b):
        def cor(x):
            is_prime = (x <= 255) and (x >= 0) and isinstance(x, int)
            return is_prime
        return cor(r) and cor(g) and cor(b)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        sid = []
        for i in sides:
            if i > 0:
                sid.append(i)
        return len(sid) > 0 and len(sides) == len(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides


    def get_sides(self):
        return [*self.__sides]

    def __len__(self, *sides):
        return sum([*self.__sides])

    def is_valid_sides_count(self, args):
        if len(args) != self.sides_count:
            args = (1,) * self.sides_count
        return args


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__sides = sides
        # self.__color = color
        if len(sides) != self.sides_count or 0 in self.__sides:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)
            print(self.__sides)

    def get_square(self):
        _radius = self.__sides[0] / (2 * pi)
        return round((pi * _radius ** 2), 1)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__sides = sides
        # self.__color = color
        if len(sides) != self.sides_count or 0 in self.__sides:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)
            print(self.__sides)

    def get_sides(self):
        return [*self.__sides]

    def get_square(self):
        p = sum([*self.__sides]) / 2
        s = (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5
        return round(s, 1)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__sides = sides
        if len(sides) != self.sides_count or 0 in self.__sides:
            a = self.__sides[0]
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(a)

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        a = (self.__sides[0])
        return a ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 9)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())

print()
print('Дополнительная проверка')

tr = Triangle((155, 200, 100), 10, 11, 10)
print(tr.get_square())
tr = Triangle((155, 200, 100),  11, 10)
print(tr.get_square())
tr.set_color(160, 66, 77)
# print(tr.get_color())
tr.set_color(300, 66, 77)
print(tr.get_color())
tr.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(tr.get_sides())
print(circle1.get_square())
cube1 = Cube((222, 35, 130), 3, 15, 0, 9, 9, 9, 12, 9, 9, 9, 5, 9,)
print(cube1.get_sides())

circle1 = Circle((200, 200, 100), 12)
print(circle1.get_square())
