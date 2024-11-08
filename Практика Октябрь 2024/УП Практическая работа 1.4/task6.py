def shaded_area(a, b):
    if not (-2 <= a <= 2):
        return False
    
    if b < -3:
        return False
    
    if b <= (5/2) * a + 2 and b <= (-5/2) * a + 2:
        return True
    
    return False

a = float(input("Введите координату a: "))
b = float(input("Введите координату b: "))

if shaded_area(a, b):
    print("Точка принадлежит заштрихованной области.")
else:
    print("Точка не принадлежит заштрихованной области.")
