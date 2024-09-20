def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    dict_string = {}
    k = 0
    for i in strings:
        k += 1
        dict_string[k, file.tell()] = i
        file.write(i + '\n')
    file.close()
    return dict_string


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
