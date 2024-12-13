# Задача 3.1
"""
Вычислить и вывести на экран сумму кубов натуральных чисел от 1 до n включительно. Верхний предел должен 
вводиться с клавиатуры и не должен превышать числа 100.
"""
print("Введите верхний предел, он не должен превышать число 100")
N = int(input())
while N > 100:
    print("Верхний предел не должен превышать число 100, введите заново")
    N = int(input())

sum_ = 0
for i in range(1, N+1):
    sum_ += i ** 3
print(f"Сумма кубов натуральных числел от 1 до {N} включительно = {sum_}")

# Задача 3.2
"""
Выведите на экран таблицу умножения чисел от одного до девяти. Красиво. С одинаковыми расстояниями
между числами.
"""
# функция форматированного вывода матрицы
def outp_matrix(matrix):
    for elem in matrix:
        for n in elem:
            print(f"{n:^4} |", end = " ")
        print()   
        print("-" * 7 * len(elem)) 

Multiplication_table = [[i * j for j in range(1,10)] for i in range(1, 10)]

outp_matrix(Multiplication_table) # выводим таблицу умножени

# Задача 3.3
"""
(*) Переверните массив на 90 градусов против часовой стрелки.

Ход рассуждения:
    # matrix[0,2] matrix[1,2] matrix[2,2]
    # matrix[0,1] matrix[1,1] matrix[2,1]
    # matrix[0,0] matrix[1,0] matrix[2,0]
"""
# функция форматированного вывода матрицы
import copy


def outp_matrix(matrix):
    for elem in matrix:
        for n in elem:
            print(f"{n:^4} |", end = " ")
        print()   
        print("-" * 7 * len(elem)) 

# Функция обеспечивает ввод двумерного массива (матрицы) с произвольным количеством строк n и столбцов m
def input_matrix():
    print("Введите количество строк n:")
    m = int(input())
    sp = list()
    for i in range(m):
        print(f"Введите элементы {i+1}-й строки через пробел")
        sp.append(list(map(int, input().split())))
    print() # отступ (пропускаем строку для удобство чтения вывода)    
    print("Исходный массив")
    outp_matrix(sp)
   
    return sp    

# Функция разворота массива на 90 градусов против часовой стрелки
def matrix_rotate(matrix):
    str_list = [] # список для строк
    row_list = [] # список для столбцов
    # цикл перебора столбцов от правого крайнего до левого крайнего
    j = len(matrix[0]) - 1
    while j >= 0:
        i = 0
        row_list.clear()
        # цикл перебора строк от первой строки до последней 
        while i < len(matrix):
            row_list.append(matrix[i][j])
            i += 1
        str_list.append(copy.copy(row_list)) 
        j -= 1    
    return str_list # возвращаем перевернутый массив


def main():
    matrix = input_matrix() # вводим двумерный массив (матрицу)
    print("Перевернутый массив на 90 градусов против часовой стрелки")
    outp_matrix(matrix_rotate(matrix)) # выводим результат (перевернутый массив)
    
    

if __name__ == '__main__':
    main()   