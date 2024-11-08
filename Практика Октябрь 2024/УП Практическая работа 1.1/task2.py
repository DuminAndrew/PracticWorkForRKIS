numbers = []
while True:
    try:
        num = int(input("Введите число: "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Введите целое число.")

if numbers:
    summa = sum(numbers)
    product = 1
    for n in numbers:
        product *= n
    average = summa / len(numbers)

    print("Сумма:", summa)
    print("Произведение:", product)
    print("Среднее:", average)
else:
    print("Список пуст.")
