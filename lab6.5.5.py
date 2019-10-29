import random
import numpy as np


f = open('input.txt', 'w')
num_1 = random.randrange(2, 8)
num_2 = random.randrange(2, 8)
num_3 = random.randrange(5, 16)
f.write('%d \n' % num_1 )
f.write('%d \n' % num_2)
f.write('%d' % num_3)
f.close()

f = open('input.txt', 'r')
lines = f.readlines()
n = lines[0][0]
m = lines[1][0]
k = lines[2]
n = int(n)
m = int(m)
k = int(k)
f.close()

matrix = [[random.randrange(10) for y in range(m)] for x in range(n)]
matrix2 = [[random.randrange(10) for y in range(k)] for x in range(m)]

matrix.sort()
matrix2.sort()


mat = np.array(matrix)
mat2 = np.array(matrix2)

total = mat.dot(mat2)

print(mat)
print()
print(mat2)
print()
print(total)
