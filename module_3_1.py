def count_calls():
    global calls
    calls += 1
    return calls


def string_info(stroka):
    kort_ = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return kort_


def is_contains(string,list_to_search):
    k = len(list_to_search)
    is_prime = False
    for i in range(0, k):
        if list_to_search[i].lower() == string.lower():
            is_prime = True
            break
    count_calls()
    return is_prime


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


