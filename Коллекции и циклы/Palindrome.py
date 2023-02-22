number = int(input("Введите число:"))

reverse_number = 0
n = number

while n > 0:
    rem = n % 10
    reverse_number = reverse_number * 10 + rem
    n = n // 10

if number == reverse_number:
    print('Palindrome')
else:
    print('No Palindrome')