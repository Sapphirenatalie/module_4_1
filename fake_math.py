from math import inf


def divide(first, second):
    try:
        result = first / second
        return result
    except ZeroDivisionError:
        return 'Ошибка'


result1 = divide(69, 3)
result2 = divide(3, 0)
print(result1)
print(result2)
