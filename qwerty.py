word = input()

for _ in range(4):
    print(word)


word = input()

i = 0
while i < 4:
    print(word)
    i +=1


print("Введите чило")
num = int(input())

while num != 0:
    print(num * 5)
    print("Введите число")
    num = int(input())

    
list_n = [1, 2, 3, 4, 5]
max1 = list_n[0]

for i in range(1, len(list_n)):
    if list_n[i] > max1:
        max1 = list_n[i]
print(max1)


list_n = [1, 2, 3, 4, 5]
i= 0
maxi = list_n[0]

while i < len(list_n):
    if list_n[i] > maxi:
        maxi = list_n[i]
    i += 1
print(maxi)


list_n = [1, 2, 3, 4, 5]
mini = list_n[0]

for i in range(1, len(list_n)):
    if list_n[i] < mini:
        mini = list_n[i]
print(mini)


list_n = [1, 2, 3, 4, 5]
i = 0
mini = list_n[0]

while i < len(list_n):
    if list_n[i] < mini:
        mini = list_n[i]
    i += 1
print(mini)


list_n = [100, 25, 398, 46, 5]
i= 0
maxi = list_n[0]

while i < len(list_n):
    if list_n[i] > maxi:
        maxi = list_n[i]
        k = i
    i += 1

print(maxi)
print(k)


def maxlist(sp):
    list_n = [0]
    max1 = list_n[0]

    for i in range(1, len(list_n)):
        if list_n[i] > max1:
            max1 = list_n[i]
    return max1

#СРЕЗЫ
s = ['сорока', 'попугай', 'пчела', 'шершень', 'луненыш']
# пример встроенных функций:
# sum(s)
# s.count(value) 
# max(s)
# min(s)
# s.insert(index,value)
# s.pop(index)
# s.remove(value)
print(s[0:2] + s[-2:]) #['сорока', 'попугай', 'шершень', 'луненыш']
print(s[0:3] +['тусон'] + s[-2:])#['сорока', 'попугай', 'пчела', 'тусон', 'шершень', 'луненыш']
print(s[::-1])#['луненыш', 'шершень', 'пчела', 'попугай', 'сорока']

'''
С клавиатуры вводится
количество лайков под каждой
Диминой публикацией до тех
пор, пока не будет введено число
-1.
Вывести “Поздравляю, ты
популярен!”, если хотя бы под
одной публикацией набралось
100 лайков или более, и “Пока ты
не обрел популярность” иначе.
'''
n = int(input())

while n != -1:
    if n >= 100:
        print("Поздравляю, ты популярен!")
        n = int(input())
    else:
        print("Пока ты не обрел популярность")
        n = int(input())


'''
Нам даны два целых числа n и m -
длина и ширина ковра.
Необходимо вывести изображение
ковра с заданными параметрами.
'''

n = int(input())
m = int(input())

for i in range(n):
    for i in range(m):
        print('x', end = ' ')
    print() #переход на следующую строку

'''
Для приготовления фруктового
салата требуются груши, яблоки
и киви. Количество единиц
каждого фрукта не играет роли
– главное, чтобы в сумме в
салате было n фруктов.
Вывести все возможные
комбинации фруктов для
приготовления салата.
'''

num = int(input())

for i in range(num + 1):
    for j in range(num + 1):
        for k in range(num + 1):
            if i + j + k == num:
                print(f"груш {i}, яблок {j}, киви {k}")
