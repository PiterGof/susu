import datetime
import timeit

radious = int(input("R: "))
center_x = int(input('x:'))
center_y = int(input('y:'))
def main(x, y, r):
    total = 0
    total2 = 0
    file = open('output4.txt', 'w')
    file.write(str(str(datetime.datetime.today()) + '\n'))
    for i in range(x + 1, r + 1):
        total += 1
    for i in range(y + 1, r + 1):
        total += 1
    total *= 2
    total += 1

    for i in range(x + 1, r):
        total2 += 1

    for i in range(y + 1, r):
        total2 += 1
    total2 *= 2
    total += total2
    file.write(str(total))
    file.close()


main(center_x, center_y, radious)
print(timeit.timeit("main(center_x, center_y, radious)", setup="from __main__ import main, center_x, center_y, radious", number=1))
