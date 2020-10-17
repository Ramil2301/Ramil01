total = 0
while True:
    n = input("Введите число или стоп для выхода: ")
    if str(n) == "стоп":
        print("Выход из программы! До встречи!")
        break # инструкция выхода из цикла
    else:
        total = total + n
        print(total)
