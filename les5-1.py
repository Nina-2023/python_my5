# Запись данных пользователя

while True:
    data = input('Введите данные: ')
    if data == '':
        break
    else:
        with open('data.txt', 'a') as f:
            f.write(data + '\n')