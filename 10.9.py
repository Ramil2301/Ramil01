s=str(input())
total=0 #сумма
kol=0 #количество
for i in range(len(s)):
    if s[i].isdigit():
        kol=kol+1
    if s[i].isalpha():  # посимвольно проверяем наличие буквы   
        continue # инструкция перехода к следующему шагу цикла
    total=total+int(s[i]) #накапливаем сумму, если встретилась цифра
print ("сумма чисел", total, ", их количество:", kol, ',max=', max(int(x) for x in s if x.isdigit()))
