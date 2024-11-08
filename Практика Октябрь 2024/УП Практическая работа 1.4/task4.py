def count_adjacent_duplicates(filename):
    with open(filename, 'r') as file:
        numbers = list(map(int, file.read().strip().split()))
        count = 0
        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i - 1]:
                count += 1
    return count

result = count_adjacent_duplicates('numsTask4.txt')
print("Количество одинаковых рядом стоящих чисел:", result)
