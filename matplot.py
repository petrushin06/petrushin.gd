import numpy as np
import matplotlib.pyplot as plt

# Параметры функции
a = 0  # точка разрыва второго рода

# Создание значений x с учетом разрыва
# Можно делать левый и правый графики и потом строить оба
x_left = np.linspace(-2, a - 0.01, 2000)  # Левее точки разрыва
x_right = np.linspace(a + 0.01, 2, 2000)  # Правее точки разрыва
# Можно сделать один, но применить plt.scatter, тогда не нужно делать два графика.
# x = np.linspace(-3, 3, 3500)
# Определение функции
def f(x):
    return 1 / (x - a**2)

# Построение графика
plt.figure(figsize=(8, 6))
# Тут через plt.plot
plt.plot(x_left, f(x_left), label=r"$f(x) = \frac{1}{x - a^{2}}$", color="blue")
plt.plot(x_right, f(x_right), color="blue")

# Тут через plt.scatter
# plt.scatter(x_left, f(x_left), label=r"$\mathcal{F} = \frac{1}{x - a}$", color="blue", s=1) # s регулирует размер маркера
# plt.scatter(x_right, f(x_right), color="blue")


# plt.scatter(x, f(x), color="darkmagenta", s=1) # Пример, когда можно юзануть функцию один раз

# Отметим точку разрыва на оси
# plt.axvline(a, color='red', linestyle='--', label='Точка разрыва')

# Настройки графика
plt.xlabel("Frequency (cm$^{-1}$)")
plt.ylabel("f(x)")
plt.title("График функции с точкой разрыва второго рода")
plt.legend()
plt.grid(True)
plt.ylim(-10, 10)  # Ограничение на ось y для наглядности
plt.show()
