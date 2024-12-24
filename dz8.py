# Задача 8.1
import re

text = input()
if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text):
    print('private')
elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', text):
    print('taxi')
else:
    print('такого нет')

# Задача 8.2
import re

text = input()
print(len(re.findall(r'\b\w[\w-]*\b', text)))

# Задача 8.3
import re

text = input()
for i in re.findall(r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)', text):
     text = text.replace(i, '(TBD)')
print(text)
ext = input()
print(re.findall(r'(?:[АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ]{2,}[ ]*)+', text))
