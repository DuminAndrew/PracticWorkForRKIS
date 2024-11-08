import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Сгенерированные числа:", numbers)
min_index = numbers.index(min(numbers))
print("Номер минимального элемента:", min_index)
