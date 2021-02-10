import math


def f(x):
    if x < -12:
        return x**5 - x**3
    elif -12 <= x < 27:
        return (math.sin(x) - abs(x)) ** 4 / 86 - math.exp(x)
    elif x > 27:
        return 55*(x**6 + abs(x))**8 + x


if __name__ == '__main__':
    print(f(4))
    print(f(79))
