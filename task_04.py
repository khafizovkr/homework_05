# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('data/for_task_04.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        line = line.split()
        line[0] = num_dict[line[0]]
        with open('data/for_task_04_russian.txt', 'a', encoding='utf-8') as f_d:
            f_d.write(' '.join(line) + '\n')