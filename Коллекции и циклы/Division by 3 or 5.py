limit = int(input('enter:'))

total_sum = 0

for x in range(limit + 1):
    if x % 3 == 0 or x % 5 == 0:
        total_sum += x
print(total_sum)

