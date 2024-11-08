def multiples(n):
    product = 1
    for i in range(3, n + 1, 3):
        product *= i
    return product

n = int(input("Введите n: "))
print("Произведение натуральных чисел с условиями - n:", multiples(n))