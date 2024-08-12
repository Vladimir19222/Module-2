def get_multiplied_digits(number):
    global stack
    str_number = str(number)
    first = int(str_number[0])
    if len(stack) > 0:
        stack.append(first*stack[len(stack) - 1])
    else:
        stack.append(first)
    print(stack)
    if len(str_number) <= 1:
        return first
    else:
        str_number = ''.join([str_number[i] for i in range(len(str_number)) if i != 0])
        number = int(str_number)
        first = first * get_multiplied_digits(number)
        return first


stack = []
result = get_multiplied_digits(40203)
print(result)
