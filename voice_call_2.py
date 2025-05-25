class GeometricShape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @staticmethod
    def is_rectangle(shape):
        return isinstance(shape, GeometricShape)

    @classmethod
    def create_square(cls, side_length):
        return GeometricShape(side_length, side_length)

    def __str__(self):
        return f"GeometricShape({self.width}, {self.height})"
    def __eq__(self, other):
        pass
    def __add__(self, other):
        pass


# Создание объекта прямоугольника
rectangle = GeometricShape(5, 3)

# Вызов обычных методов
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

# Вызов статического метода
print("Is Rectangle:", GeometricShape.is_rectangle(rectangle))

# Создание квадрата с использованием метода класса
square = GeometricShape.create_square(4)

# Магический метод для представления объекта в виде строки
print(rectangle)  # Вывод: GeometricShape(5, 3)
print(square)  # Вывод: GeometricShape(4, 4)