strings = []
while True:
    user = input("Введите строку: ")
    if user == "":
        break
    strings.append(user)

if strings:
    short_est = min(strings, key=len)
    long_est = max(strings, key=len)
    print("Самый короткий элемент:", shor_test)
    print("Самый длинный элемент:", long_est)
else:
    print("Список пуст.")
