import math


def f(n):
    if not n:
        return 4
    return 1/82 * f(n-1) - math.sin(f(n-1))


if __name__ == '__main__':
    print(f(5))
    print(f(16))
