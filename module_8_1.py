def add_everything_up(a, b):
    res = 0
    try:
        res = a + b
    except TypeError as exc:
        res = str(a) + str(b)
        # print(exc)
    finally:
        if isinstance(res, float):
            res = round(res, 3)
        return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('гру', 'ша'))
