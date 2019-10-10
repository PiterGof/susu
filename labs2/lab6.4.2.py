import os
directory = 'B:/pyProjescts/'
files = os.listdir(directory)
total = 0
total_2 = 1

if 'input2.txt' in files:
    file = open('input2.txt', 'r')
    number = int(file.read())
    for i in str(number):
        total += int(i)
        total_2 *= int(i)
    file2 = open('output2.txt', 'w')
    file2.write('Число: %d \n' % number)
    file2.write('Количество цифр: %s \n' % len(str(number)))
    file2.write('Сумма цифр: %d \n' % total)
    file2.write('Произведение цифр: %d' % total_2)
    file2.close()
    file.close()
else:
    print('Файл с входными данными не обнаружен')