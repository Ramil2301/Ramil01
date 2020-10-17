n = input()
if all(map(str.isdigit, n)):
    sm = 0
    n = list(map(int, n))
    for i in n:
        if i % 2 != 0:
            sm += i**2
    print(sm)
else:
    print('Error')
