#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.
not_exit = True
with open('txt_file.txt', 'w') as f:
    while not_exit:
        line = input('Запись в файл: ')
        if line == '':
            not_exit = False
            break
        f.write(line + '\n')


