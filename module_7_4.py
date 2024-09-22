def form(team1_num, team2_num):
    print('В команде %s участников: %s !' % ('Мастера кода', team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

def f_ormat(score_2, team1_time):
    print('Команда Волшебники решила задач: {}!'.format(42))
    print('{} решили задачи за {} cек. !'.format(score_2, team1_time))

def f_stroka(team1_time, team2_time):
    print(f'Команды решили {score_1} и {score_2} задач.')
    average_time = round((team1_time + team2_time)/(score_1 + score_2), 1)
    print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {average_time} секунды на задачу!')
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    print(f'Результат битвы: {result}')


form(5, 6)
f_ormat('Волшебники', 2153.31451)
score_1 = 40
score_2 = 42
f_stroka(1552.512, 2153.31451)