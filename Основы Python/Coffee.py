print('Добрый день')
cup = int(input('Сколько чашек кофе вы желаете?\n'))
bonus_cup = cup // 6

if cup // 6:
    print(f'Количество бонусных чашек кофе - {bonus_cup} шт')
elif 0 < cup < 6:
    print('Количество бонусных чашек кофе - 0 шт')