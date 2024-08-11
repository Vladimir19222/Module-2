def print_params(a=1, b='строка', c=True):
    print(a, b, c)

def print_params1(**kwargs):
    print(kwargs)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    print(list_my)

print('1.Функция с параметрами по умолчанию:')
print_params()
print_params(3, 12, 15)
print_params(a=23,c=17)
print_params(c=15,b='Dima')
print_params(b=25)
print_params(c=[1,2,3])

print()
print('2.Распаковка параметров:')
values_list = [True, 5, 'кролик']
values_dist = {'a': 4127, 'b': 'Dima', 'c': False}
print_params(*values_list)
print_params(**values_dist)
print_params1(**values_dist)
print()
print('3.Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
values_list_2 = [False, [1, 2]]
print_params(*values_list_2, 42)
print()
print('4.Функция def append_to_list')
append_to_list('Bim', list_my=None)