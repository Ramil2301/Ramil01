s=str(input())
total=0
for i in range(len(s)):
    if s[i].isalpha(): # посимвольно проверяем наличие буквы
        continue # инструкция перехода к следующему шагу цикла
    total=total+str(s[i]) #накапливание количества букв
for max(len(s)): # для слова максимально длины
    print s.index() #индекс длинного слова    
