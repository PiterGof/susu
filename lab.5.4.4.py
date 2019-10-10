sum = int(input('Sum: '))

def main(sum):
    rub = sum // 100
    kop = sum % 100
    if rub % 10 in range(5, 10) or kop % 100 in range(10, 21) or kop % 10 == 0 and kop % 10 in range(5, 10) or kop % 100 in range(10, 21) or kop % 10 == 0:
        print(('%s рублей' % rub).upper())
        print(('%s копеек' % kop).upper())
    elif rub % 10 in range(2, 5) and rub % 100 not in range(12, 15) and kop % 10 in range(2, 5) and kop % 100 not in range(12, 15):
        print(('%s рубля' % rub).upper())
        print(('%s копки' % kop).upper())
    else:
        print(('%s рубль' % rub).upper())
        print(('%s копека' % kop).upper())
main(sum)
