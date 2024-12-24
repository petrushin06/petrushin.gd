'''
Напишите программу, которая запрашивает у пользователя возраст и проверяет:

    Если возраст меньше 18, выводится сообщение "Вам ещё рано!".
    Если возраст в диапазоне от 18 до 65, выводится сообщение "Добро пожаловать!".
    Если возраст больше 65, выводится сообщение "Берегите здоровье!".

age = int(input("Введите ваш возраст: "))

if age < 18:  # Условие для первой категории
    print("Вам ещё рано!")
elif 18 <= age <= 65:  # Условие для второй категории
    print("Добро пожаловать!")
else:
    print("Берегите здоровье!"
'''
'''
Напишите программу, которая находит сумму всех чётных чисел в заданном диапазоне, включая границы.

start = int(input())  # Начало диапазона
end = int(input())  # Конец диапазона



# Используйте цикл для нахождения суммы
sum_even = 0

for i in range(start, end + 1):
    sum_even += i 
print(f"Сумма чётных чисел от {start} до {end}: {sum_even}")
'''

'''
Напишите программу, которая вычисляет факториал заданного числа с использованием цикла.

# Реализуйте вычисление факториала

number = int(input("Введите число: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i


print(f"Факториал числа {number}: {factorial}")
'''

'''
Напишите программу, которая определяет, является ли заданный год високосным.

# Реализуйте проверку високосного года

year = int(input("Введите год: "))

if year % 4 == 0:  # Условие для високосного года
    print(f"{year} год является високосным.")
else:
    print(f"{year} год не является високосным.")
'''

'''
Напишите программу, которая находит максимальное и минимальное значение в списке чисел.

# Найдите максимум и минимум

numbers = [10, -3, 5, 7, 9, 0, -1]
max_num = numbers[0] # Максимум
min_num = numbers[0] # Минимум
i = 0

while i < len(numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1
while i < len(numbers):
    if numbers[i] < min_num:
        min_num = numbers[i]
    i += 1

print(f"Максимальное значение: {max_num}")
print(f"Минимальное значение: {min_num}")
'''

'''
Создайте программу, которая хранит цены на несколько товаров в словаре. Затем запросите у пользователя название товара и выведите его цену.

# Создайте словарь с ценами товаров

prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 70,
    "груша": 100
}

product = input("Введите название товара: ")

# Проверьте наличие товара в словаре
if product in prices:
    print(f"Цена на {product}: {prices[product]} руб.")
else:
    print("Такого товара нет в списке.")
'''
'''
Напишите функцию, которая принимает координаты двух точек на плоскости и возвращает расстояние между ними. Используйте формулу:

расстояние=(x2 − x1)2+(y2 − y1)2−−−−−−−−−−−−−−−−−−√

# Реализуйте функцию расчёта расстояния

import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Формула расчёта

# Пример вызова функции
x1, y1 = 0, 0
x2, y2 = 3, 4

distance = calculate_distance(x1, y1, x2, y2)
print(f"Расстояние между точками: {distance:.2f}")
'''

'''
Напишите программу, которая переводит температуру из градусов Цельсия в градусы Фаренгейта и наоборот. Пользователь должен выбрать направление перевода.
'''
'''
# Реализуйте перевод температуры

def celsius_to_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

choice = input("Выберите перевод (1: Цельсий -> Фаренгейт, 2: Фаренгейт -> Цельсий): ")
if choice == '1':
    print(celsius_to_fahrenheit(int(input("Введите значение в градусах Цельсия"))))
elif choice == '2':
    print(fahrenheit_to_celsius(int(input("Введите значение в градусах Фарингейта"))))
'''

'''
Описание: Постройте графики функций y1=x^3−x и y2=2x−1 на интервале [−3,3]. Найдите численно приближённые точки пересечения и отметьте их на графике.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Определение функций
def f1(x):
    return x**3 - x

def f2(x):
    return 2*x - 1

# Разница функций для нахождения пересечений
def diff(x):
    return f1(x) - f2(x)

# Нахождение точек пересечения
x_roots = fsolve(diff, [-2, 0, 2])  # Три предположительных корня
y_roots = f1(x_roots)

plt.plot(x_roots, y_roots)
x = np.arange(-3, 3, 0.01)
plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.scatter(x_roots, y_roots, color='#FFD0EC', edgecolors='#1F2544',
linewidth=2, s=40)
plt.show()
'''

'''
Описание: Постройте графики функций y1=sin(x) и y2=cos(x) на интервале [0,2π]. Добавьте сетку, легенду и отметьте основные точки пересечения с осью абсцисс.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x = np.linspace(0, 2 * np.pi)   
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.grid()
plt.legend (('sin(x)', 'cos(x)'))
x1_roots = np.array([0, np.pi, np.pi * 2]) 
x2_roots = np.array([np.pi/2, np.pi * 3/2]) 
y1_roots = np.sin(x1_roots)
y2_roots = np.cos(x2_roots)

plt.scatter(x1_roots, y1_roots, color='#FFD0EC', edgecolors='#1F2544', linewidth=2, s=40)
plt.scatter(x2_roots, y2_roots, color='#FFD0EC', edgecolors='#1F2544', linewidth=2, s=40)


plt.show()
'''

'''
Напишите функцию, которая переводит угол из градусов в радианы. Проверьте работу функции на примере углов 0°, 90°, 180° и 360°.


# Реализуйте перевод градусов в радианы

import math

def degrees_to_radians(degrees):
    return degrees * math.pi / 180  # Формула перевода

# Примеры вызова функции
angles = [0, 90, 180, 360] # выдать список радиан
for angle in angles:
    radians = degrees_to_radians(angle)

    print(f"{angle}° = {radians:.2f} радиан")
'''

'''
Напишите программу, которая генерирует случайный список из 10 чисел в диапазоне от 1 до 100 и выводит его на экран


# Генерация случайного списка

import random

random_list = [random.randint(1, 100) for _ in range(10)]  # Используйте random.sample или random.randint

print("Случайный список:", random_list)
'''

'''

1. Напишите функцию, которая принимает два аргумента:
    список товаров
    товар, который нужно найти.
2.Если товар присутствует в списке, то вернуть индекс первого вхождения. Учтите, что товаров может быть несколько.
3.Если товар не найден в списке, то вернуть None.

# Напишите функцию для поиска индекса товара
def find(items_list, find_item):
    flag = False
    i = 0
    while i < len(items_list) and not flag:
        if items_list[i] == find_item:
            flag = True
        if not flag:    
            i += 1        
    if flag:
        return i
    else:
        return None   


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find(items_list, find_item)  # Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
'''
        
'''
Постройте график логарифмической функции y=ln(x) на интервале [0.1,10]. Добавьте сетку, легенду и отметьте основные точки.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 5000)
y = np.log(x)  # Логарифмическая функция
plt.plot(x, y, color='#ff0000', label = "ln(x)")

plt.title("График функции y = ln(x)")
ax = plt.gca()
ax.set_xlabel("x", fontsize=15) # подписываем ось X
ax.set_ylabel("f(x)", fontsize=15) # подписываем ось Y



plt.grid()
plt.legend(loc='best')# Подпись самой функции
plt.show()
'''

'''
У вас есть список чисел, в котором один из элементов случайно пропущен.
Ваша задача — найти пропущенный элемент и заменить его средним арифметическим всех остальных элементов списка.
При расчете суммы для среднего арифметического берутся все числа, кроме пропуска.
А для расчёта количества — все элементы, включая пропуск.

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_list = numbers[:numbers.index(None)] + numbers[numbers.index(None) + 1:]
summa = 0

for i in new_list:
    summa += i
sr_ar = summa / len(numbers)# Среднее арифметическое
new_list.insert(numbers.index(None), sr_ar)# insert - вставляет на место (1 аргумент) другое (2 аргумент)
print("Измененный список:", new_list)
'''
'''
У вас есть список players, который содержит имена игроков.
Вам необходимо определить общее количество игроков в списке и затем с использованием слайсирования разделить игроков на две равные команды.
Распечатайте каждую команду участников на отдельной строке.

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(*first_team)
print(*second_team)
'''


'''
Напишите функцию find_common_participants, принимающую две строки, в которых перечислены участники без пробелов, а также необязательный аргумент, отвечающий за разделитель по умолчанию равен запятой.
Найдите общих участников среди двух групп.
Верните полученный результат в виде списка общих участников отсортированных в алфавитном порядке.
 
# Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separate = ',' ):
    first_list = participants_first_group. split(separate)
    second_list = participants_second_group. split(separate)
    result_list = []
    for elem in first_list:
        if elem in second_list:
            result_list.append(elem)
    result_list.sort()# sort - сортировка по алфавиту 
    return result_list


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(*find_common_participants(participants_first_group, participants_second_group))

# Проверьте работу функции с разделителем отличным от запятой
'''
