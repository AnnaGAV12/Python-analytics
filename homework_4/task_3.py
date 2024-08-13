# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date

MULTIPLICITY = 50
RICHNESS_AMOUNT = 5_000_000
PERCENT_BONUS  = 0.03
PERCENT = 0.015
PERCENT_RICHNESS = 0.01
MIN_LIMIT = 30
MAX_LIMIT = 600
COUNT_PERC = 3

balance = 0
count = 0
percent_take = 0.015
percent_tax = 0.01

def add_balance(cash: float) -> None:
    global balance
    global count
    balance += cash
    count += 1
    if count % 3 == 0:
        balance = balance + PERCENT_BONUS * balance
        print(f'Начислены проценты в размере: {PERCENT_BONUS * balance}')

def take_balance(cash: float) -> None:
    global balance
    global count
    balance -= cash
    count += 1

    if cash * PERCENT < MIN_LIMIT:
        balance -= MIN_LIMIT
        print(f'Списаны проценты за снятие денег: {MIN_LIMIT}')
    elif cash * PERCENT > MAX_LIMIT:
        balance -= 600
        print(f'Списаны проценты за снятие денег: {MAX_LIMIT}')
    else:
        balance -= cash * PERCENT
        print(f'Списаны проценты за снятие денег: {cash * PERCENT}')
    if count % COUNT_PERC == 0:
        balance = balance + PERCENT_BONUS * balance
        print(f'Начислены проценты в размере: {PERCENT_BONUS * balance}')


def exit_bank():
    print('Мы рады вас снова увидеть!')
    exit()

def check_balance() -> int:
    while True:
        cash = int(input(f'Введите сумму кратную {MULTIPLICITY}: '))
        if cash % MULTIPLICITY == 0:
            return cash

list_operation = []

while True:
    action = input("1 - Снять деньги\n2 - Пополнить счет\n3 - Текущий баланс\n4 - Вывести историю операций\n5 - Выйти\nВведите действие: ")

    if action == '1':
        if balance > RICHNESS_AMOUNT:
            balance = balance - balance * PERCENT_RICHNESS
            print(f'Списан налог на богатство в размере: {balance * PERCENT_RICHNESS}')
        cash = check_balance()
        if cash < balance:
            take_balance(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print('No money')
        if balance > RICHNESS_AMOUNT:
            balance = balance - balance * PERCENT_RICHNESS
            print(f'Списан налог на богатство в размере: {balance * PERCENT_RICHNESS}')
        print(f'Текущий баланс: {balance}')
    elif action == '2':
        cash = check_balance()
        add_balance(cash)
        if balance > RICHNESS_AMOUNT:
            balance = balance - balance * PERCENT_RICHNESS
            print(f'Списан налог на богатство в размере: {balance * PERCENT_RICHNESS}')
        print(f'Текущий баланс: {balance}')

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print(f'Текущий баланс: {balance}')
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()