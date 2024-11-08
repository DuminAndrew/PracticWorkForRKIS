import random

original = [random.uniform(-10, 10) for _ in range(10)]
positive = [num for num in original if num > 0]
negative = [num for num in original if num < 0]

print("Исходный массив:", original)
print("Положительные элементы:", positive)
print("Отрицательные элементы:", negative)
