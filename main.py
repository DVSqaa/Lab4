# Імпортуємо необхідні бібліотеки
import math
import matplotlib.pyplot as plt

# Визначаємо клас Point_n
class Point_n:
    # Змінна класу для відслідковування кількості створених екземплярів
    count = 0

    # Конструктор з двома параметрами (за замовчуванням)
    def __init__(self, x=0, y=0):
        # Встановлюємо координати точки, перевіряючи їх на відповідність діапазону [-100, 100]
        self.__x = self.__check_coordinate(x)
        self.__y = self.__check_coordinate(y)
        # Збільшуємо кількість створених екземплярів
        Point_n.count += 1

    # Деструктор, що виводить відповідне повідомлення
    def __del__(self):
        print("Об'єкт видалено")

    # Метод для перевірки координат на відповідність діапазону [-100, 100]
    def __check_coordinate(self, value):
        if -100 <= value <= 100:
            return value
        else:
            return 0

    # Геттер для координати x
    @property
    def x(self):
        return self.__x

    # Сеттер для координати x
    @x.setter
    def x(self, value):
        self.__x = self.__check_coordinate(value)

    # Геттер для координати y
    @property
    def y(self):
        return self.__y

    # Сеттер для координати y
    @y.setter
    def y(self, value):
        self.__y = self.__check_coordinate(value)

    # Метод класу, що повертає кількість створених екземплярів
    @classmethod
    def get_count(cls):
        return cls.count

    # Метод, що змінює координати точки
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Функція для розрахунку відстані між двома точками
def distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Створюємо список з трьох точок
points = [Point_n(10, 10), Point_n(20, 20), Point_n(30, 30)]

# Розраховуємо відстань між другою і третьою точкою
dist = distance(points[1], points[2])
print(f"Відстань між другою і третьою точкою: {dist}")

# Переміщаємо першу точку на 20 вниз і на 30 вправо
points[0].move(-20, 30)

# Візуалізуємо точки
x_values = [point.x for point in points]
y_values = [point.y for point in points]

plt.plot(x_values, y_values, 'ro')
plt.grid()
plt.show()
