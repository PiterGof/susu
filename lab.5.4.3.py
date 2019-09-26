hours_start = int(input('Hours start: '))
minutes_start = int(input('Minutes start: '))
hours_way = int(input('Hours way: '))
minutes_way = int(input('Minutes way: '))
days = hours_way
total_hours = 0
total_min = 0
def time(h_s, m_s, h_w, m_w, t_h, t_m, days):
    t_h = h_s + h_w
    t_m = m_s + m_w

    if t_h >= 24:
        t_h2 = t_h - 24
        t_h = t_h2
        if t_h >= 24:
            t_h = 0
    if t_m >= 60:
        t_m2 = t_m - 60
        t_m = t_m2
        t_h += 1
        days += 1

    if t_h <= 9 and t_m <= 9:
        print("0%s hours : 0%s minutes" % (t_h, t_m))
        print('%s days' % (days // 24))
    elif t_h <= 9:
        print("0%s hours : %s minutes" % (t_h, t_m))
        print('%s days' % (days // 24))
    elif t_m <= 9:
        print("%s hours : 0%s minutes" % (t_h, t_m))
        print('%s days' % (days // 24))
    else:
        print("%s hours : %s minutes" % (t_h, t_m))
        print('%s days' % (days // 24))

time(hours_start, minutes_start, hours_way, minutes_way, total_hours, total_min, days)