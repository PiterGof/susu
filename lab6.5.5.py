import random

f = open('input.txt', 'w')
num_1 = random.randrange(2, 8)
num_12 = random.randrange(2, 8)
f.write('%d' % num_1 )
f.write('%d' % num_12)
f.close()

f = open('input.txt', 'r')
lines = f.readline()
n = lines[0]
m = lines[1]
n = int(n)
m = int(m)
f.close()

matrix = [[random.randrange(10) for y in range(m)] for x in range(n)]
matrix2 = [[random.randrange(10) for y in range(m)] for x in range(n)]


for i in range(n):
    print(matrix[i])
    print((matrix2[i][i]))
    print('Hello')


for i in range(n):
    print(matrix[i])

print(' ')
for i in range(n):
    print(matrix2[i])

# for i in matrix:
#     for k in matrix2:
#         for a in k:
#             for j in i:
#                 print(a*j)
