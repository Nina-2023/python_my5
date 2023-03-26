with open('text_file.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    with open('new_file.txt', 'w', encoding='utf-8') as new_f:
        for line in content:
            line = line.replace('One', 'Один')
            line = line.replace('Two', 'Два')
            line = line.replace('Three', 'Три')
            line = line.replace('Four', 'Четыре')
            new_f.write(line)

