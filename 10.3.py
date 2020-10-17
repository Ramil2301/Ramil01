import random

def listgen(n):
    mlist = [random.randint(-10, 10) for i in range(n)]  # получаем список
    print(mlist)  # выводим
    print(mlist[n // 2:])  # прваая половина
    print(mlist[:n // 2])  # левая
if __name__ == '__main__':
    n = int(input())
    listgen(n)