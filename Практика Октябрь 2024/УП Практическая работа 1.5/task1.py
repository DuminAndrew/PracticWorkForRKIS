def after_min(filename):
    with open(filename, 'r') as file:
        numbers = list(map(int, file.read().split()))
    
    min_index = numbers.index(min(numbers))
    product = 1
    for num in numbers[min_index + 1:]:
        product *= num
    
    return product

result1 = after_min('numsTask1.txt')
print("Произведение элементов после минимального:", result1)
