player1 = input('Введите имя первого игрока:\n')
player2 = input('Введите имя второго игрока:\n')

sticks = 10

while sticks > 0:
    move1 = int(input(f'{player1} Введите значение от 1 до 3:\n'))
    while move1 < 1 or move1 > 3:
        move1 = int(input(f'{player1} Введите значение от 1 до 3:\n'))
    sticks -= move1
    print(f'Осталось {sticks} палочек')
    if sticks == 0:
        print(f'{player1} Вы проиграли')
        break

    move2 = int(input(f'{player2} Введите значение от 1 до 3:\n'))
    while move2 < 1 or move2 > 3:
        move2 = int(input(f'{player2} Введите значение от 1 до 3:\n'))
    sticks -= move2
    print(f'Осталось {sticks} палочек')
    if sticks == 0:
        print(f'{player2} Вы проиграли')
        break