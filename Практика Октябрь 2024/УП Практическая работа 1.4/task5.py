def shaded_area(a, b):
    if -2 <= a <= 4 and -3 <= b <= 4:
        return True
    return False

a = float(input("Введите координату a: "))
b = float(input("Введите координату b: "))

if shaded_area(a, b):
    print("Точка принадлежит заштрихованной области.")
else:
    print("Точка не принадлежит заштрихованной области.")
