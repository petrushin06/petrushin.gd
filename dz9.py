"""
Цель задания - исследование функции
при различных значениях а и в.
Для каждой задачи необходимо:
• Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций),
график каждой функции должен быть одного цвета для одного значения а и В.
• Подписать оси и заголовок
• Создать легенду
• Создать сетку
• Сохранить изображение в svg файл

Задача 1 
Построить в общих осях графики для:
• a=1,ß=1
• a=2,ß=1
• a=1,ß=2

"""
import os
import numpy as np
import math
import matplotlib.pyplot as plt

dir = os.getcwd()
a = 0  # точка разрыва второго рода
x1_left = np.linspace(-10, a - 0.01, 2000)  # Левее точки разрыва
x1_right = np.linspace(a + 0.01, 10, 2000)  # Правее точки разрыва


plt.title("График функции f(x) = " + r"$\frac{x^b+a^b}{x^b}$")

plt.grid(visible=True)
ax = plt.gca()
ax.set_xlabel("x", fontsize=15) # подписываем ось X
ax.set_ylabel("f(x)", fontsize=15) # подписываем ось Y
# график 1
a  = 1
b = 1
y1_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y1_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва

plt.plot(x1_left, y1_left, color ='#ff0000', label = "a=1, b=1")
plt.plot(x1_right, y1_right, color ='#ff0000')


# график 2
a  = 2
b = 1
y2_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y2_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва
plt.plot(x1_left, y2_left, color ='#1c02ff', label = "a=2, b=1")
plt.plot(x1_right, y2_right, color ='#1c02ff')

# график 3
a  = 1
b = 2
y3_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y3_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва
plt.plot(x1_left, y3_left, color ='#02ff0f', label = "a=1, b=2")
plt.plot(x1_right, y3_right, color ='#02ff0f')

plt.legend () # создаем легенду (подписываем графики)


plt.xlim(-5, 5)  # Ограничение на ось x для наглядности
plt.ylim(-5, 5)  # Ограничение на ось y для наглядности

plt.savefig(dir + '/task_9_1', dpi=300) # сохраняем графики в файл

plt.show()

"""
Цель задания - исследование функции
при различных значениях а и в.
Для каждой задачи необходимо:
• Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций),
график каждой функции должен быть одного цвета для одного значения а и В.
• Подписать оси и заголовок
• Создать легенду
• Создать сетку
• Сохранить изображение в svg файл

Задача 2
Построить в общих осях графики для x>0.
На том же графике сделать 2 врезки, демонстрирующие поведение графиков на 2 интервалах:
• для малых х
• для больших х
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций.
Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений а и В.

"""
import os
import numpy as np
import math
import matplotlib.pyplot as plt

dir = os.getcwd()
new_graph = plt.figure()
a = 0  # точка разрыва второго рода
x1_left = np.linspace(-1000, a - 0.01, 200000)  # Левее точки разрыва
x1_right = np.linspace(a + 0.01, 1000, 200000)  # Правее точки разрыва


plt.title("График функции f(x) = " + r"$\frac{x^b+a^b}{x^b}$")

plt.grid(visible=True)
ax = plt.gca()
ax.set_xlabel("x", fontsize=15) # подписываем ось X
ax.set_ylabel("f(x)", fontsize=15) # подписываем ось Y
# график 1
a  = 1
b = 1
y1_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y1_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва

plt.plot(x1_left, y1_left, color ='#ff0000', label = "a=1, b=1")
plt.plot(x1_right, y1_right, color ='#ff0000')


# график 2
a  = 2
b = 1
y2_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y2_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва
plt.plot(x1_left, y2_left, color ='#1c02ff', label = "a=2, b=1")
plt.plot(x1_right, y2_right, color ='#1c02ff')

# график 3
a  = 1
b = 2
y3_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y3_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва
plt.plot(x1_left, y3_left, color ='#02ff0f', label = "a=1, b=2")
plt.plot(x1_right, y3_right, color ='#02ff0f')

plt.legend () # создаем легенду (подписываем графики)


plt.xlim(0, 10)  # Ограничение на ось x для наглядности
plt.ylim(0, 10)  # Ограничение на ось y для наглядности

# врезки
cut1 = new_graph.add_axes([0.2,0.62,0.2,0.25])  # размер (x, y, width, height)
cut1.plot(x1_right, y1_right, color ='#ff0000')#добавляем график на врезку
cut1.plot(x1_right, y2_right, color ='#1c02ff')#добавляем график на врезку
cut1.plot(x1_right, y3_right, color ='#02ff0f')#добавляем график на врезку
plt.xlim(0, 0.2) 
plt.ylim(1, 1000) 


cut2 = new_graph.add_axes([0.5,0.62,0.2,0.25]) # размер (x, y, width, height)
cut2.plot(x1_right, y1_right, color ='#ff0000')#добавляем график на врезку
cut2.plot(x1_right, y2_right, color ='#1c02ff')#добавляем график на врезку
cut2.plot(x1_right, y3_right, color ='#02ff0f')#добавляем график на врезку
plt.xlim(998, 999) 
plt.ylim(0.99, 1.01) 

plt.savefig(dir + '/task_9_2', dpi=300) # сохраняем графики в файл

plt.show()

"""
Цель задания - исследование функции
при различных значениях а и в.
Для каждой задачи необходимо:
• Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций),
график каждой функции должен быть одного цвета для одного значения а и В.
• Подписать оси и заголовок
• Создать легенду
• Создать сетку
• Сохранить изображение в svg файл

Задача 3
Построить в общих осях графики для x<0.
На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении х от 0 к -∞.
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций. Так же нанесите на
графики прямую f(x) = 0.
Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений а и В.

"""
import os
import numpy as np
import math
import matplotlib.pyplot as plt

dir = os.getcwd()
new_graph = plt.figure()
a = 0  # точка разрыва второго рода
x1_left = np.linspace(-1000, a - 0.01, 20000)  # Левее точки разрыва
x1_right = np.linspace(a + 0.01, 1000, 20000)  # Правее точки разрыва


plt.title("График функции f(x) = " + r"$\frac{x^b+a^b}{x^b}$")

plt.grid(visible=True)
ax = plt.gca()
ax.set_xlabel("x", fontsize=15) # подписываем ось X
ax.set_ylabel("f(x)", fontsize=15) # подписываем ось Y
# график 1
a  = 1
b = 1
y1_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y1_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва

plt.plot(x1_left, y1_left, color ='#ff0000', label = "a=1, b=1")
plt.plot(x1_right, y1_right, color ='#ff0000')


# график 2
a  = 2
b = 1
y2_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y2_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва
plt.plot(x1_left, y2_left, color ='#1c02ff', label = "a=2, b=1")
plt.plot(x1_right, y2_right, color ='#1c02ff')

# график 3
a  = 1
b = 2
y3_left = (x1_left ** b + a ** b)/ (x1_left ** b) # Левее точки разрыва
y3_right = (x1_right ** b + a ** b)/ (x1_right ** b) # Правее точки разрыва
plt.plot(x1_left, y3_left, color ='#02ff0f', label = "a=1, b=2")
plt.plot(x1_right, y3_right, color ='#02ff0f')

plt.axvline(0, color='red', linestyle='--', label='f(x) = 0')

plt.legend(loc ="best") # создаем легенду (подписываем графики)






plt.xlim(-10, 0.01)  # Ограничение на ось x для наглядности
plt.ylim(-10, 10)  # Ограничение на ось y для наглядности

# врезки
cut1 = new_graph.add_axes([0.5,0.62,0.2,0.25])  # размер (x, y, width, height)
cut1.plot(x1_left, y1_left, color ='#ff0000')#добавляем график на врезку
cut1.plot(x1_left, y2_left, color ='#1c02ff')#добавляем график на врезку
cut1.plot(x1_left, y3_left, color ='#02ff0f')#добавляем график на врезку
plt.xlim(-999, -998) 
plt.ylim(0.99, 1.01) 


plt.savefig(dir + '/task_9_3', dpi=300) # сохраняем графики в файл

plt.show()

"""
4. Построить в общих осях графики для:
• a=1,ß=0.5
• a=1,ß=-0.5
• a=1,ß=-1.5
Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость
В результате выполнения предыдущей задачи, вы вероятно заметите, что все графики с a=1 проходят через общую точку (1, 2).
Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.
Каждый график будет содержать 4 кривые. 2 общих:
• a=1,ß=0 (в качестве цвета попробуйте использовать 'b-)
• a=1,ß=-1 (в качестве цвета попробуйте использовать 'г-)
И по 2 уникальных для каждого графика:
• a=1,ß=0.5 и
• a=1,ß=0.8
• a=1,ß=-0.5 и
• a=1,ß=-0.8
• a=1,8=-1.5 и
• a=1,ß=-2.5
Не забудьте добавить легенду на каждый график. Для этого может потребоваться вызвать метод legend() для каждого объекта
осей.
Для того чтобы задать общий заголовок для всех 3 графиков используйте метод https://matplotlib.org/api/_as_gen/
matplotlib.pyplot.suptitle.html
"""
import os
import numpy as np
import math
import matplotlib.pyplot as plt

dir = os.getcwd()
new_graph = plt.figure()

x = np.linspace(0, 1000, 200000)  



plt.title("График функции f(x) = " + r"$\frac{x^b+a^b}{x^b}$")

plt.grid(visible=True)
ax = plt.gca()
ax.set_xlabel("x", fontsize=15) # подписываем ось X
ax.set_ylabel("f(x)", fontsize=15) # подписываем ось Y
# график 1
a  = 1
b = 0.5
y1 = (x ** b + a ** b)/ (x ** b) 


plt.plot(x, y1, color ='#ff0000', label = "a=1, b=0.5")



# график 2
a  = 1
b = -0.5
y2 = (x ** b + a ** b)/ (x ** b) 
plt.plot(x, y2, color ='#1c02ff', label = "a=1, b=-0.5")


# график 3
a  = 1
b = -1.5
y3 = (x ** b + a ** b)/ (x ** b) 

plt.plot(x, y3, color ='#02ff0f', label = "a=1, b=-1.5")


plt.legend () # создаем легенду (подписываем графики)


plt.xlim(0, 10)  # Ограничение на ось x для наглядности
plt.ylim(0, 10)  # Ограничение на ось y для наглядности



plt.savefig(dir + '/task_9_4', dpi=300) # сохраняем графики в файл

plt.show()

"""
Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.
Каждый график будет содержать 4 кривые. 2 общих:
• a=1,ß=0 (в качестве цвета попробуйте использовать 'b-)
• a=1,ß=-1 (в качестве цвета попробуйте использовать 'г-)
И по 2 уникальных для каждого графика:
• a=1,ß=0.5 и
• a=1,ß=0.8
• a=1,ß=-0.5 и
• a=1,ß=-0.8
• a=1,8=-1.5 и
• a=1,ß=-2.5
Не забудьте добавить легенду на каждый график. Для этого может потребоваться вызвать метод legend() для каждого объекта
осей.
Для того чтобы задать общий заголовок для всех 3 графиков используйте метод https://matplotlib.org/api/_as_gen/
matplotlib.pyplot.suptitle.html
"""
import os
import numpy as np
import math
import matplotlib.pyplot as plt
dir = os.getcwd()
plt.title("График функции f(x) = " + r"$\frac{x^b+a^b}{x^b}$")

ax1 = plt.subplot(1, 3, 1) 
ax2 = plt.subplot(1, 3, 2) 
ax3 = plt.subplot(1, 3, 3) 
ax1.grid(visible=True)
ax2.grid(visible=True)
ax3.grid(visible=True)

ax2.set_xlabel("x", fontsize=15) 
ax1.set_ylabel("f(x)", fontsize=15) 

x = np.linspace(0, 10, 2000) 
# график 1.1
a  = 1
b = 0
y1 = (x ** b + a ** b)/ (x ** b) 
ax1.plot(x, y1, color = 'blue', label = "a=1, b=0")


# график 1.2
a  = 1
b = -1
y1 = (x ** b + a ** b)/ (x ** b) 
ax1.plot(x, y1, color = 'green', label = "a=1, b=-1")


# график 1.3
a  = 1
b = 0.5
y1 = (x ** b + a ** b)/ (x ** b) 
ax1.plot(x, y1, color = "#154691ff", label = "a=1, b=0.5")


# график 1.4
a  = 1
b = 0.8
y1 = (x ** b + a ** b)/ (x ** b) 
ax1.plot(x, y1, color = "#914d15ff", label = "a=1, b=0.8")


# график 2.1
a  = 1
b = 0
y1 = (x ** b + a ** b)/ (x ** b) 
ax2.plot(x, y1, color = 'blue', label = "a=1, b=0")


# график 2.2
a  = 1
b = -1
y1 = (x ** b + a ** b)/ (x ** b) 
ax2.plot(x, y1, color = 'green', label = "a=1, b=-1")


# график 2.3
a  = 1
b = -0.5
y1 = (x ** b + a ** b)/ (x ** b) 
ax2.plot(x, y1, color = "#154691ff", label = "a=1, b=-0.5")


# график 2.4
a  = 1
b = -0.8
y1 = (x ** b + a ** b)/ (x ** b) 
ax2.plot(x, y1, color = "#914d15ff", label = "a=1, b=-0.8")



# график 3.1
a  = 1
b = 0
y1 = (x ** b + a ** b)/ (x ** b) 
ax3.plot(x, y1, color = 'blue', label = "a=1, b=0")


# график 3.2
a  = 1
b = -1
y1 = (x ** b + a ** b)/ (x ** b) 
ax3.plot(x, y1, color = 'green', label = "a=1, b=-1")


# график 3.3
a  = 1
b = -1.5
y1 = (x ** b + a ** b)/ (x ** b) 
ax3.plot(x, y1, color = "#154691ff", label = "a=1, b=-1.5")


# график 3.4
a  = 1
b = -2.5
y1 = (x ** b + a ** b)/ (x ** b) 
ax3.plot(x, y1, color = "#914d15ff", label = "a=1, b=-2.5")

ax1.legend()
ax2.legend()
ax3.legend()

plt.savefig(dir + '/task_9_5', dpi=300) 

plt.show()


