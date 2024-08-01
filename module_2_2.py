first = input('Введите 1-ое число: ')
second = input('Введите 2-ое число: ')
third  = input('Введите 3-ое число: ')
if first == second  and second == third:
    print('3')
elif first == second or first == third:
    print('2')
elif second == first or second == third:
    print('2')
else:
    print('0')