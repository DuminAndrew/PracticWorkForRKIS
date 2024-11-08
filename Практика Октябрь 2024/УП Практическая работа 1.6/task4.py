a = int(input("Введите положительное число a: "))
total_sum = 0

while True:
    number = int(input("Введите положительное число: "))
    if number < 0:
        break
    if number % a == 0:
        total_sum += number

print("Сумма чисел, делящихся на a:", total_sum)
