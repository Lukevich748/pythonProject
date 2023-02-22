import random

i = random.randint(1, 50)

attempts = 6

while attempts != 0:
    attempt = int(input('Введите число:'))
    attempts = attempts - 1
    if i > attempt:
        print('Число больше')
    if i < attempt:
        print('Число меньше')
    elif i == attempt:
        print('Ура, Вы угадали число')
        break
    elif attempts == 0:
        print(f"Уппсс, попытки иссякли, мое число: {i}")
