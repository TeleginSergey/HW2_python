num = int(input())

maxnum = 0
count = 0

while num != 0:
    #если введёное число больше максимального - оно и есть максимальное 
    if num > maxnum:
        maxnum = num
        #Если нашли наибольшее снова, то счёт наибольшего прошлого убираем
        count = 0
    elif num == maxnum:
        count += 1
    num = int(input())
#+1 т.к. мы должны учесть первую цифру(программа считает кол-во "=")
print(count+1)