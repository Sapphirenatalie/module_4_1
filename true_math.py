from math import inf


def divide(first, second):
    try:
        result = first / second        
        return result
    except ZeroDivisionError:
        return inf


result1 = divide(49, 7)
result2 = divide(15, 0)
print(result1)
print(result2)
