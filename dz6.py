# Задача 6.1
"""
Дан двумерный массив размером 3х3. Определить максимальное значение среди элементов третьего столбца массива;
максимальное значение среди элементов второй строки массива. Вывести полученные значения.
"""
#arr = [[3, 4, 11], [12, 33, 10], [9, 2, 21]] для проверки

# функция форматированного вывода матрицы
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
    outp_matrix(sp)
   
    return sp    

    
def main():
    # цикл поиска максимального значения среди элементов 3 столбца массива
    arr = input_matrix() # вводим двумерный массив (матрицу)
    max_ = 0
    for st in arr: # перебираем строки
        if st[2] > max_: # проверяем значение третьего столбца в строке st
            max_ = st[2]

    # цикл поиска максимального значения среди элементов 2 строки массива        
    max2 = 0        
    for column in arr[1]:  # перебираем столбцы во второй строке
        if column > max2:
            max2 = column


    print(f"Максимальное значение среди элементов третьего столбца массива = {max_}") 
    print(f"Максимальное значение среди элементов второй строки массива = {max2}")       

if __name__ == '__main__':
    main()

# Задача 6.2
"""
Дан двумерный массив размером mхn. Сформировать новый массив заменив положительные элементы единицами, 
а отрицательные нулями, вывести оба массива
arr = [[3, -1, 11], [-9, 33, 10], [-5, 2, -1]] для проверки
"""

# функция форматированного вывода матрицы
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
        
    #print() # отступ (пропускаем строку для удобство чтения вывода)    
    #for elem in sp: 
        #print(*elem) # показываем введенную матрицу
    return sp    

def main():
    from copy import deepcopy # подключаем библиотеку для копирования изменяемых данных
    arr = input_matrix() # вводим двумерный массив (матрицу)
    arr2 = deepcopy(arr) # двумерный массив (вложенный список) можно скопировать только глубоким копированием
    for m in arr2:
        for i in range(len(m)):
            if m[i] > 0:
                m[i] = 1
            else:
                m[i] = 0

    print("Исходный массив:")
    outp_matrix(arr)

    print("Новый массив:")
    outp_matrix(arr2)   

if __name__ == '__main__':
    main()

# Задача 6.3
"""
Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т.е. такой матрицей, в 
в которой суммы элементов во всех строках и столбцах одинаковы.
https://ru.m.wikipedia.org/wiki/Магический_квадрат
matrix1 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]] # пример магического квадрата 3х3
matrix2 = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]] # пример магического квадрата 4х4
matrix3 = [[2, 8, 6], [9, 5, 1], [6, 3, 8]] # пример не магического квадрата 3х3
"""

# функция форматированного вывода матрицы
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
    outp_matrix(sp)
   
    return sp     

""" Функция принимает матрицу, возвращает логическое True, если матрица не является магическим квадратом 
или False, есил матрица является магическим квадратом"""
def matrix_control(matrix):
    sp = [] # список для хранения сумм строк
    sp2 = [] # список для хранения сумм столбцов
    
    # цикл проверки сумм строк
    for m in matrix:
        sp.append(sum(m))    
    # цикл проверки сумм столбцов
    for j in range(len(matrix[0])):
        summa = 0
        for st in matrix:
            summa += st[j]
        sp2.append(summa)  
    # цикл проверки суммы элементов главной диагонали
    summa = 0
    i = 0
    for m in matrix:
        summa += m[i]
        i+= 1
    main_summa = summa    
    # цикл проверки сумм элементов побочной диагонали
    summa = 0
    i = len(matrix[0]) - 1
    for m in matrix:
        summa += m[i]
        i -= 1
    side_summa = summa 

    sp_col_st = sp + sp2  # общий список сумм строк и столбцов 
   
    # цикл проверки на равенство сумм строк, столбцов и диагоналей
    flag = False
    if main_summa == side_summa: # если суммы диагоналей равны
        i = 0
        while i < len(sp_col_st) and not flag:
            if sp_col_st[i] != main_summa: # если суммы в общем списке сумм строк и столбцов равны сумме элементов диагонали (любой)
                flag = True 
            i += 1
    else:
        flag = True # если суммы диагоналей не равны, то квадрат не является магическим и дальше не проверяем       

        
    return flag 

def main():
    matrix = input_matrix() # вводим двумерный массив (матрицу)
    if not matrix_control(matrix):
        print("Матрица является магическим квадратом")
    else:
        print("Матрица не является магическим квадратом")
                 


if __name__ == '__main__':
    main()   

# Задача 6.4
"""
Определить, является ли заданная целая квадратная матрица n-го порядка
симметричной (относительно главной диагонали)
Примеры симметричных матриц:
1 3 0
3 2 6
0 6 5

 2  1  5 -4  
 1  6  3 -9  
 5  3  8  7  
-4 -9  7  3  
Рассуждения: 
a33 (3)
a23 = a32 (7)
a13 = a31 (-9)
a03 = a30 (-4)

a22 (8)
a12 = a21 (3)
a02 = a20 (5)

a11 (6)
a01 = a10 (1)

matrix1 = [[1, 3, 0], [3, 2, 6], [0, 6, 5]] # пример симметричной матрицы
matrix2 = [[2, 1, 5, -4], [1, 6, 3, -9], [5, 3, 8, 7], [-4, -9, 7, 3]] # примет симметричной матрицы
matrix3 = [[2, 9], [9, 5]] # пример симметричной матрицы
matrix4 = [[2, 8, 6], [9, 5, 1], [6, 3, 8]] # примет не симметричной матрицы
"""

# функция форматированного вывода матрицы
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
    outp_matrix(sp)
   
    return sp    

# Функция получает на вход матрицу, возвращает логическое False, если матрица 
# симметричная относительно главной диагонали
def matrix_control(matrix):
        flag = False
        j = 1
        while j < len(matrix) and not flag:
            for i in range(0, j):
                if matrix[i][j] != matrix[j][i]:
                    flag = True
            j += 1   
        return flag # True, если матрица не симметричная                

def main():
    matrix = input_matrix() # вводим двумерный массив (матрицу)
    if not matrix_control(matrix):
        print("Матрица симметричная")
    else:
        print("Матрица не симметричная")          
    
if __name__ == '__main__':
    main()   


# Задача 6.5
"""
Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. 
Вывести на печать найденные строки и суммы их элементов.


matrix1 = [[7, 16, 18, 14], [2, 13, 5, 11], [16, 30, 10, 10]] # пример прямоугольной матрицы
"""
# функция форматированного вывода матрицы
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
    outp_matrix(sp)
   
    return sp    

# Функция принимает матрицу, возвращает строку с минимальной суммой элементов и ее номер начиная с 1
def min_str_matrix(matrix):
    minim = sum(matrix[0])
    index = 0
    for i in range(1, len(matrix)):
        if sum(matrix[i]) < minim:
            minim = sum(matrix[i]) 
            index = i
    return f"Наименьшая сумма элементов = {minim} (строка № {index + 1})"    

# Функция принимает матрицу, возвращает строку с максимальной суммой элементов и ее номер начиная с 1
def max_str_matrix(matrix):
    maxim = sum(matrix[0])
    index = 0
    for i in range(1, len(matrix)):
        if sum(matrix[i]) > maxim:
            maxim = sum(matrix[i]) 
            index = i
    return f"Наибольшая сумма элементов = {maxim} (строка № {index + 1})"    

def main():
    matrix = input_matrix() # вводим двумерный массив (матрицу)
    print(max_str_matrix(matrix))
    print(min_str_matrix(matrix))

if __name__ == '__main__':
    main()    


# Задача 6.6
"""
Дана действительная матрица размером nхm, все элементы которой различны. В каждой строке
выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем,
нечетное - единицей. Вывести на экран новую матрицу.

matrix1 = [[4, 16, 18, -2], [1, 13, 5, 11], [15, 30, -8, 10]] # пример матрицы
"""
# функция форматированного вывода матрицы
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
        sp.append(list(map(float, input().split())))
    print() # отступ (пропускаем строку для удобство чтения вывода)    
    outp_matrix(sp)
   
    return sp  

# Функция принимает список (одномерный массив), возвращает список с заменненными значениями согласно условию задачи
def minim_bin(sp):
    sp_result = []
    for elem in sp:
        if elem == min(sp):
            if elem % 2 == 0:
                sp_result.append(0.0)
            else:
                sp_result.append(1.0)
        else:
            sp_result.append(elem)       
    return sp_result             
                
# Функция принимает матрицу, возвращает матрицу с заменными значениями согласно условию задачи
def ch_matrix(matrix):
    return [minim_bin(elem) for elem in matrix]


def main():
    matrix = input_matrix()
    new_matrix = ch_matrix(matrix)
    print("Новая матрица")
    outp_matrix(new_matrix)

if __name__ == '__main__':
    main()   