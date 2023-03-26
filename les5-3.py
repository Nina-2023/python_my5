with open('test_file.txt', 'w+') as f:
    f.write('Иванов 23543.12\n')
    f.write('Петров 13749.32\n')
    f.write('Сидоров 26500.00\n')
    f.write('Смирнов 18000.00\n')
    f.write('Попов 16000.00\n')
    f.write('Кузнецов 24000.00\n')
    f.write('Осинцев 19000.00\n')
    f.write('Кравцов 15000.00\n')
    f.write('Соловьев 30000.00\n')
    f.write('Степанов 25500.00\n')

f = open('test_file.txt', 'r')

sum_salaries = 0
low_salaries_employees = []

for line in f:
    employee, salary = line.split()
    sum_salaries += float(salary)
    if float(salary) < 20000:
        low_salaries_employees.append(employee)

avg_salary = sum_salaries / 10.0

print(f'Сотрудники с окладом менее 20 тысяч: {", ".join(low_salaries_employees)}')
print(f'Средняя величина дохода сотрудников: {avg_salary}')

f.close()