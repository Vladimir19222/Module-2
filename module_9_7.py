def is_prime(func):
    def wrapper(*args):
        logics = True
        for i in range(2, func(*args) // 2 + 1):
            if func(*args) % i == 0:
                logics = False
                break
        if logics:
            print("Простое")
        else:
            print("Составное")
        return func(*args)
    return wrapper


@is_prime
def sum_three(*numb):
    return sum([*numb])


result = sum_three(2, 3, 6)
print(result)
