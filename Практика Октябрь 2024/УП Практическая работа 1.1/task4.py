def generation_random_numbers(start, end):
    return [random.randint(start, end) for _ in range(10)]

begin = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
numbers = generation_random_numbers(begin, end)

print("Случайные числа:")
for index, value in enumerate(numbers):
    print(f"{index} -> {value}")
