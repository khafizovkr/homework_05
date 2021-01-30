# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
lines = 0
symbols = 0
with open('data/readme.txt', 'r') as f:
    for line in f:
        lines += 1
        for symbol in line:
            symbols += 1
print(f'В файле {symbols} символов и {lines} строк')