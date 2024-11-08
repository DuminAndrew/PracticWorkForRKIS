a = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

new_column = []
for row in a:
    count_of_ones = sum(row)
    new_column.append(1 if count_of_ones % 2 != 0 else 0)

for i in range(len(a)):
    a[i].append(new_column[i])

for row in a:
    print(row)