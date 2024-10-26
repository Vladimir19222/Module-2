import matplotlib.pyplot as plt
import pandas as pd
import requests
import math
from PIL import Image
from io import BytesIO

"""
  Pandas — это пакет для манипулирования табличными данными в Python, то есть данными в виде строк и столбцов,
также известными как DataFrames.  
  Функциональность pandas включает в себя преобразование данных. При помощи pandas можно сортировать строки и выделять 
подмножества, вычислять сводную статистику, например, среднее значение, изменять формы фреймов и объединять их.
"""

print()
print('Чемпионат по футболу:')

football_team = ['Спартак', 'ЦСКА', 'Динамо', 'Локомотив', 'Буревестник']
football = {'Команда': football_team,
        'Забитые голы': [207, 193, 189, 173, 148],
        'Очки': [27, 24, 20, 12, 9],
        'Лучший игрок': ['Иван Пеле', 'Н. Мбаппе', 'П. Беккенбауэр', 'С. Голенищев', 'О. Гризманн']}

# вывести таблицу:

df = pd.DataFrame(football)
print(df)

# сохранить в таблице excel:

with pd.ExcelWriter('table.xlsx', engine='xlsxwriter') as wb:
    df.to_excel(wb, sheet_name='Sheet1', index=False)
    sheet = wb.sheets['Sheet1']
    sheet.set_column('A:A', 20)
    sheet.set_column('B:B', 15)
    sheet.set_column('C:C', 6)
    sheet.set_column('D:D', 20)

print()

"""
  Matplotlib — это обширная библиотека для создания статичных, анимированных и интерактивных визуализаций.
Она используется для создания любых видов графиков: линейных, круговых диаграмм, построчных гистограмм и других.
"""

x = [- math.pi / 2 + ((math.pi * z) / 10) for z in range(41)]
y = [math.sin(z) for z in x]
y1 = [0.02 * z ** 2 - 1 for z in x]
plt.title('графики периодической функции y = sin(x) и параболы')
plt.plot(x, y, marker='1')
plt.plot(x, y1, marker='1')
plt.xlabel('X')
plt.ylabel('Y1')
plt.ylabel('Y')
plt.show()

"""
  Библиотека изображений pillow (Python) добавляет возможности обработки изображений в  интерпретатор Python.
Эта библиотека обеспечивает широкую поддержку форматов файлов, эффективное внутреннее представление и довольно мощные
возможности обработки изображений.
"""

image_url = 'https://i.postimg.cc/43qrydQ8/image.jpg'
response = requests.get(image_url)
if response.status_code == 200:
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    resized_image = image.resize((500, 500))
    resized_image.save('resized.jpg')
    rot_image = Image.open('resized.jpg').rotate(45, expand=True)
    rot_image.save('resized1.png')
    image1 = Image.open('resized.jpg')
    image1.show()
    image1.close()
else:
    print("Failed to fetch the image. Status code:", response.status_code)
