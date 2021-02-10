import math


def f(x: float):
    return math.sqrt(x ** 6 + x + 33) - (93*x**7 + 25*x**3)/\
           (math.cos(x) - 14*x + 79) + (math.tan(x) + x**3)/\
           (x**7 - 57*x**8)


if __name__ == '__main__':
    print(f(-94))
    print(f(-33))

print(__name__)
