import random

should_continue = True
while should_continue:
    user = input('Выберите значение: [R/S/P]\n').lower()

    if user not in ['r', 's', 'p']:
        print('Неверный ввод, выберите одно из значений')
        continue

    gen = {1: 'r', 2: 's', 3: 'p'}
    computer = gen[random.randint(1, 3)]
    print(f'Выбор компьютера: {computer}')

    win = [('r', 's'), ('s', 'p'), ('p', 'r')]

    if user == computer:
        print('Ничья')
    elif (user, computer) in win:
        print('Вы выиграли')
    else:
        print('Выиграл компьютер')

    should_continue = input('Играем [yes/no]?').lower() == 'yes'
