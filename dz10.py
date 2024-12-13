# Задача 1
"""
Создать объект pandas Series или Dataframe из списка, объекта NumPy (массива), и словаря
"""
import numpy as np
import pandas as pd

# создание объекта Series
# создаем объект pandas Series из списка
sp = [1, 4, 6, 8, 10, 12]
p1 = pd.Series(sp)
print(p1)

# создаем объект pandas Series из массива NumPy
nmp_arr = np.array([1, 4, 6, 8, 10, 12])
p2 = pd.Series(nmp_arr)
print(p2)

# создаем объект pandas Series из словаря
dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
p3 = pd.Series(dic)
print(p3)

# создание объекта Dataframe
# создаем объект pandas Dataframe из двумерного списка
sp2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
p4 = pd.DataFrame(sp2)
print(p4)

# создаем объект pandas Dataframe из двумерного массива NumPy 
nmp_arr2 = np.array(sp2)
p5 = pd.DataFrame(nmp_arr2)
print(p5)

# создаем объект pandas Dataframe из словаря
dic2 = ({"country":['Russia', 'Belarus', 'China'], 
            "population": [143.8, 9.2, 1411],
            "square": [17125191,207560, 9579000]
})
p6 = pd.DataFrame(dic2)
print(p6)

# Задача 2
""" Получить не пересекающиеся элементы в двух объектах 
Series или двух столбцах одного Dataframe """
import numpy as np
import pandas as pd

p1 = pd.Series([1, 9, 3, 6, 5], index=['a', 'b', 'c', 'd', 'e'])
p2 = pd.Series([1, 5, 3, 4, 9], index=['a', 'b', 'c', 'd', 'e'])

p3 = pd.concat([p1, p2], axis=0) # объединяем Series по индексам
p3 = pd.concat([p1, p2], axis=0).value_counts() # value_counts() показывает, как часто элементы встречаются в Series
p3 = p3[p3 < 2] # выводим элементы (индексы), которые встречаются в объединенном Series один раз
print(*p3.index)

# Задача 3
""" Узнать частоту уникальных элементов объекта Series или в одной колонке (можно для нескольких) Dataframe, и построить
гистограмму (семейство гистограмм) с помощью plt.bar() """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p = pd.Series([1, 4, 3, 4, 5, 3], index=['a', 'b', 'c', 'd', 'e', 'f'])
p = p.value_counts()
print(p)

plt.bar(p.index, p.values)

plt.show()

# Задача 4
"""
Объединить два объекта Dataframe вертикально (конкатенация: pd. concat() ) 
и горизонтально (добавить столбцы: df .insert()
"""
import numpy as np
import pandas as pd

# Создаём два DataFrame
df1 = pd.DataFrame({"id": [1, 2, 3], 
                    "name": ["Алексей", "Николай", "Александр"],
                    "surname": ["Иванов", "Петров", "Сидоров"]
})

df2 = pd.DataFrame({"id": [9, 10, 11], 
                    "name": ["Дмитрий", "Андрей", "Пётр"],
                    "surname": ["Калинин", "Зверев", "Николаев"]
})


# Конкатенация по строкам
result = pd.concat([df1, df2], axis=0)
result.insert(3, "age", [24, 36, 40, 15, 18, 50])

print(result)

# Задача 5
"""
Попробовать построить график зависимости одного столбца от другого для Dataframe (можно несколько, т.е. создать
семейство кривых на одном графике).
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.DataFrame({
                    'x': [-10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})
df1['y1'] = df1['x'] * 2
df1['y2'] = df1['x'] * (-2) + 3

print(df1['x'])
plt.title("График функции")
plt.grid(visible=True)
plt.plot(df1['x'], df1['y1'])
plt.plot(df1['x'], df1['y2'])
plt.show()