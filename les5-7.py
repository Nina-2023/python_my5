# Создание и заполнение текстового файла

with open('firms_data.txt', 'w') as f:
    f.write('firm_1 ООО 10000 5000\n')
    f.write('firm_2 ИП 20000 4500\n')
    f.write('firm_3 Группакомпаний 30000 6000\n')

# Прочтение файла

with open('firms_data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# Вычисление прибыли каждой компании и средней прибыли

total = 0
count = 0

with open('firms_data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split(' ')
        name = data[0]
        revenue = int(data[2])
        costs = int(data[3])
        profit = revenue - costs
        if profit > 0:
            total += profit
            count += 1
        print('Прибыль компании {} составляет {}'.format(name, profit))

if count > 0:
    print('Средняя прибыль среди компаний составляет {}'.format(total / count))
else:
    print('Нет положительной прибыли')

# Реализация списка и сохранение в json

import json

total = 0
count = 0
firms_data = {}

with open('firms_data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split(' ')
        name = data[0]
        revenue = int(data[2])
        costs = int(data[3])
        profit = revenue - costs
        firms_data[name] = profit
        if profit > 0:
            total += profit
            count += 1

if count > 0:
    average_profit = total / count
else:
    average_profit = 0

data = [firms_data, {'average_profit': average_profit}]

with open('firms_data.json', 'w') as f:
    json.dump(data, f)