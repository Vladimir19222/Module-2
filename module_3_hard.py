def calculate_structure_sum(args):
    global sum
    args1 = list()
    for i in (args):
        if isinstance(i, str):
            sum += len(i)
        elif isinstance(i, int):
            sum += i
        elif isinstance(i, list):
            for j in i:
                args1.append(j)
        elif isinstance(i, tuple) or isinstance(i, set):
            m_list = list(i)
            args1.append(m_list)
        elif isinstance(i, dict):
            my_list = list(i.items())
            args1.append(my_list)
        else:
            continue
    if len(args1) > 0:
        calculate_structure_sum(args1)
    return sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0
result = calculate_structure_sum(data_structure)
print(result)
