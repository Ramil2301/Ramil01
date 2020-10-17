import random
n=random.randint(-10, 10)
while True:
    text = input("Введите число или стоп для выхода: ")
    if text == "стоп":
        print("Выход из программы! До встречи! Загадано было", n)
        break # инструкция выхода из цикла
    elif int(text) == n:
        print("Победа")
    else:
        print("Попробуйте еще")
