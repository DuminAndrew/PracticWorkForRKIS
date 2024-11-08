def sum_diff(filename):
    with open(filename, 'r') as file:
        numbers = list(map(int, file.read().split()))
    
    max_value = max(numbers)
    sum_diff = sum(num for num in numbers if num == max_value - 1)
    
    return sum_diff

result4 = sum_diff('numsTask4.txt')
print("Сумма элементов: ", result4)
