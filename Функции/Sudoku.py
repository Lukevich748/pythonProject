def any_duplicates(matrix):
    plain = [i for x in matrix for i in x]
    return print(sorted(plain) != [1, 2, 3, 4, 5, 6, 7, 8, 9])

any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]])