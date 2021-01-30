#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
sum = 0
with open('data/for_task_05.txt', 'w', encoding='utf-8') as f:
    for i in range(randint(3, 10)):
        number = randint(0, 100)
        f.write(str(number) + ' ')
        sum += int(number) #сумма считается в цикле
    f.write('\nСумма чисел = ' + str(sum))

print(sum)

#сумма считывается из файла
sum_from_file = 0
with open('data/for_task_05.txt', 'r') as f:
    line = f.readline().split()
    for number in line:
        sum_from_file += int(number)
print(sum_from_file)