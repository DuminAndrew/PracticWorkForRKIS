def before_min(filename):
    with open(filename, 'r') as file:
        numbers = list(map(int, file.read().split()))
    
    min_index = numbers.index(min(numbers))
    if min_index == 0:
        return 0
        
    average = sum(numbers[:min_index]) / min_index
    return average

result3 = before_min('numsTask3.txt')
print("Среднее арифметическое элементов до минимального:", result3)
