import math


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number):
    """Печатает квадратный корень."""
    if your_number < 0:
        your_number = 0
    your_number = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {your_number}')


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)
print(message)
calc(25.5)
