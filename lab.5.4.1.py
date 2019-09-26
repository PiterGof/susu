side_a = float(input('Side a: '))
side_b = float(input('Side b: '))
side_c = float(input('Side c: '))

def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b < c or a + c < b or b + c < a:
        print('Треугольник не существует')
    elif a == b == c:
        print('Треугольник равносторонний')

    elif (a == b or a == c or b == c) and (a + b >= c or a + c >= b or b + c >= a):
        print('Треугольник равнобедренный')

    elif a + b >= c or a + c >= b or b + c >= a:
        print('Треугольник общего вида')

triangle(side_a, side_b, side_c)
