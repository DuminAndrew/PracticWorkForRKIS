def F(filename):
    numbers = []
    with open(filename, 'r') as file:
        numbers = file.read().strip().split(',')
        for i, num in enumerate(numbers):
            value = int(num)
            if value == 0:
                numbers = numbers[:i]
                break
    if numbers:
        min_value = min(map(int, numbers))
        max_value = max(map(int, numbers))
        return min_value / max_value if max_value != 0 else None
    return None

result = F('numsTask3.txt')
print("Отношение минимального и максимального элементов:", result)