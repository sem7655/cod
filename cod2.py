lst = [1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 9, 9]
repeats = []

for i in lst:
    if lst.count(i) > 1 and i not in repeats:
        repeats.append(i)
print(repeats , lst)
