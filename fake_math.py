from math import inf


def divide(first, second):
    try:
        result = first / second
        if first > 0 and second > 0:
            if result > 0:
                return result
    except ZeroDivisionError:
        return 'Ошибка'


result1 = divide(69, 3)
result2 = divide(3, 0)
print(result1)
print(result2)
