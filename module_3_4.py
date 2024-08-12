def single_root_words(root_word, *other_words):
    same_words = []
    log = False
    for x in other_words:
        if root_word.lower() in x.lower():
            log = True
            slovo = root_word.lower()
            break
        elif x.lower() in root_word.lower():
            log = True
            slovo = x.lower()
            break
        else:
            continue
    if log == True:
        k = len(other_words)
        for i in range(0, k):
            if slovo in other_words[i].lower():
                same_words.append(other_words[i])
    else:
        same_words.append('Нет общего слова')
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
print(single_root_words('дуплище', 'Одубеть', 'дУбасить', 'дупло', 'дуБина', 'ДУБ'))
