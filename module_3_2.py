def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    log = proverka(recipient) and proverka(sender)
    if log == False:
        print("Невозможно отправить письмо с адреса", sender, "на адрес",recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender,  "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    return sender


def proverka(a):
    log1 = False
    log2 = False
    for i in range(0, len(a)):
        if a[i] == '@':
            log1 = True
            break
    if a[-3:] == '.ru' or a[-4:] == '.com' or a[-4:] == '.net':
        log2 = True
    return log1 and log2


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
    sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
