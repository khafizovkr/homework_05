# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
low_wage_employees = ''
number_of_employees = 0
salary_fund = 0
with open('data/for_task_03.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        line = line.split()
        salary_fund += int(line[1])
        number_of_employees += 1
        if int(line[1]) < 20000:
            low_wage_employees += line[0] + ', '
average_salary = salary_fund / number_of_employees
print(f'Сотрудники с окладом менее 20 тыс.: {low_wage_employees}')
print(f'Средняя величина дохода сотрудников: {round(average_salary)}')