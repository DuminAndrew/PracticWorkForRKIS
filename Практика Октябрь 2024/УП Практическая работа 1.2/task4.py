import random

def generate_temp():
    return [[random.randint(-10, 35) for _ in range(30)] for _ in range(12)]

def average_temp(temp):
    averages = []
    for month in temp:
        averages.append(sum(month) / len(month))
    return averages

temp = generate_temp()
monthlyAverages = average_temp(temp)
sortedAverages = sorted(monthlyAverages)
print(sortedAverages)
