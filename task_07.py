# 7.Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

with open('data/for_task_07.txt', 'r', encoding='utf-8-sig') as f:
    firms = [line.split()[0] for line in f]

with open('data/for_task_07.txt', 'r', encoding='utf-8-sig') as f:
    profit = [int(line.split()[2]) - int(line.split()[3]) for line in f]

positive_profit = list(filter(lambda profit_pos: profit_pos > 0, profit))
average_profit = sum(positive_profit) / len(positive_profit)

with open('data/for_task_07.json', 'w') as new_f:
    json.dump([dict(zip(firms, profit)), {'average_profit': round(average_profit, 2)}], new_f)
