number = int(input('Enter value:'))

for n in range(number + 1):
    if n % 2 == 0:
        print(f'{n} is EVEN')
    else:
        print(f'{n} is ODD')
