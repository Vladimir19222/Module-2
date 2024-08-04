numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in range(1, len(numbers)):
    for j in range(2, numbers[i]-1):
        if numbers[i] % j == 0:
            Not_Primes.append(numbers[i])
            break
    if numbers[i] not in Not_Primes:
        Primes.append(numbers[i])
print(Primes)
print(Not_Primes)