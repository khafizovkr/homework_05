# 1. Мы потеряли все точки в предложении, но можем разрезать по заглавным буквам.
# Сделать split() по заглавным бувам.
new_data = ''

with open('for_additional_task_01.txt', 'r', encoding='utf-8-sig') as f:
    data = f.read().split()
    for word in data:
        for symbol in word:
            print(symbol)
            if symbol.isupper():
                word = '*' + word
                new_data += word + ' '
                # чтобы по всему слову не шла итерация
                break
            else:
                new_data += word + ' '
                # чтобы по всему слову не шла итерация
                break

print(new_data.split('*'))