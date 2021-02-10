import math


def f(n):
    left_sum = 0
    right_sum = 0
    for i in range(1, n + 1):
        left_sum += i ** 5 - math.cos(i)
        right_sum += 26 * (abs(i) + 61 * i ** 5)
    return left_sum + right_sum


if __name__ == '__main__':
    print(f(31))
    print(f(30))
