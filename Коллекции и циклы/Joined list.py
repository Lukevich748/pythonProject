first_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

joined_lst = []

for x in first_lst:
    if x % 2 != 0:
        joined_lst.append(x)
for x in second_lst:
    if x % 2 == 0:
        joined_lst.append(x)
print(joined_lst)
