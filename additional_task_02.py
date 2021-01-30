# 2. У нас в папке лежат файлы и скрипты вместе. Нужно сделать папку data и в нее сложить все, кроме .py скриптов
import os
import shutil

os.makedirs('data', exist_ok=True)
files = os.listdir()
for file in files:
    print(file)
    if file.endswith('.txt') or file.endswith('.json'):
        shutil.move(file, 'data')
