import os
directory = 'B:/pyProjescts/'
files = os.listdir(directory)

if 'input3.txt' in files:
    file = open('input3.txt', 'r')
    n = int(file.read())
    file2 = open('output3.txt', 'w')
    for i in range(1, n):
        file2.write(str(i))
    file2.close()
    file.close()
else:
    print('Файл с входными данными не обнаружен')