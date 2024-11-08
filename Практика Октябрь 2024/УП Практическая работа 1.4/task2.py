def sumPositive(filename):
    total_sum = 0
    with open(filename, 'r') as file:
        numbers = file.read().strip().split(';')
        for num in numbers:
            value = float(num)
            if value == 0:
                break
            if value > 0:
                total_sum += value
    return total_sum

result = sumPositive('numsTask2.txt')
print("Сумма положительных элементов до первого нуля:", result)
