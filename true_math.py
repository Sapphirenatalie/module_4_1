from math import inf


def divide(first, second):
    try:
        result = first / second
        if first > 0 and second > 0:
            if result > 0:
                return result
    except ZeroDivisionError:
        return inf


result1 = divide(49, 7)
result2 = divide(15, 0)
print(result1)
print(result2)