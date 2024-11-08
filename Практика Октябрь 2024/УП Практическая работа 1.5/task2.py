def sort_floats(filename):
    with open(filename, 'r') as file:
        numbers = list(map(float, file.read().split(';')))
    
    numbers.sort()
    
    with open(filename, 'w') as file:
        file.write(';'.join(map(str, numbers)))

sort_floats('numsTask2.txt')
print("Числа отсортированы и записаны обратно")
