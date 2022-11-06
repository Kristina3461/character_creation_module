from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')


def calculatesquareroot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Выводит результат."""
    if your_number <= 0:
        return
        room = calculatesquareroot(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          'Это будет: ')


print(message)
calc(25.5)
