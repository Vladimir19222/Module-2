from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
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

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__radius = self.get_sides()[0] // 2

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(*sides)
        self.__height = [self.sides_count ** 0.5 / 2 * i for i in self.get_sides()]

    def get_height(self, side=0):
        return self.__height

    def get_square(self):
        return self.__height * self.get_sides()[0] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__sides = sides
        if len(sides) != self.sides_count:
            a = self.__sides[0]
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(a)

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return int(self.__sides[0]) ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
