def generateDict():
    months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
              "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    temp_dict = {month: [random.randint(-10, 35) for _ in range(30)] for month in months}
    return temp_dict

def average_temp_dict(temp_dict):
    averages = {}
    for month, temps in temp_dict.items():
        averages[month] = sum(temps) / len(temps)
    return averages

temp_dict = generateDict()
monthly_averages = average_temp_dict(temp_dict)
print(monthly_averages)
