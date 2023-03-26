# Открытие файла
file_name = 'data.txt'
file_handle = open(file_name, 'r')

# Подсчет строк и слов
num_lines = 0
num_words = 0
for line in file_handle:
    words = line.split()
    num_lines += 1
    num_words += len(words)

# Вывод результата
print('Количество строк:', num_lines)
print('Количество слов:', num_words)

# Закрытие файла
file_handle.close()

