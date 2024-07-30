# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:

from random import randint
def guess_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    COUNT_TRY = 10
    RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
    for _ in range(COUNT_TRY + 1):
        number = int(input('Введи число от 0 до 1000: '))
        if number > RAND_NUMBER:
            print('Ваше число БОЛЬШЕ загаданного')
        elif number < RAND_NUMBER:
            print('Ваше число МЕНЬШЕ загаданного')
        else:
            print('Вы выиграли!')

guess_number()