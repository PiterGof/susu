a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

a = float("%.5f" % a)
b = float("%.5f" % b)
c = float("%.5f" % c)

def smth(a, b, c):
    d = b**2 - 4*a*c
    x1 = (-b + d**.5) / (a * 2)
    x2 = (-b - d**.5) / (a * 2)

    print(d)
    if a == 0 or d < 0:
        print('(%.5f) * X^2 + (%.5f) * X + (%.5f) = 0' % (a, b, c))
        print('Количество корней: 0')

    elif d == 0:
        print('(%.5f) * X^2 + (%.5f) * X + (%.5f) = 0' % (a, b, c))
        print('Количество корней: 1')
        print(x1)
        print(x2)

    else:
        print('(%.5f) * X^2 + (%.5f) * X + (%.5f) = 0' % (a, b, c))
        print('Количество корней: 1')
        if x1 > x2:
            print(x1)
            print(x2)

        else:
            print(x2)
            print(x1)

smth(a, b, c)