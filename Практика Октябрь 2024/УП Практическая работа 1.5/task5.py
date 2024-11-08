def between_min_max(filename):
    with open(filename, 'r') as file:
        numbers = list(map(int, file.read().split()))
    
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    
    if min_index > max_index:
        min_index, max_index = max_index, min_index
    
    if max_index - min_index <= 1:
        return 0
    
    average = sum(numbers[min_index + 1:max_index]) / (max_index - min_index - 1)
    return average

result5 = between_min_max('numsTask5.txt')
print("Среднее арифметическое элементов между минимальным и максимальным:", result5)
