def code(n):
    cod_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                cod_ += str(i) + str(j)
    return cod_
k = input("Введите число: ")
print(code(int(k)))