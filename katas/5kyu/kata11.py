"""
Codewars 5 kyu kata: Finding an appointment
URL: https://www.codewars.com/kata/525f277c7103571f47000147/python
"""


def t2n(time):
    h, m = (int(i) for i in time.split(':'))
    return (h - 9) * 60 + m

def n2t(num):
    h = ('' if num / 60 else '0') + str(num / 60 + 9)
    m = ('' if num - num / 60 * 60 else '0') + str(num - num / 60 * 60)
    return ':'.join([h, m])

def overlaps(period1, period2):
    return period1[0] <= period2[0] < period1[1] or period2[0] <= period1[0] < period2[1]

def get_start_time(schedules, duration):
    day = []
    end_times = set([0])

    for appointments in schedules:
        for start, end in appointments:
            day.append([t2n(start), t2n(end)])
            end_times.add(t2n(end))

    for end_time in sorted(end_times):
        if end_time + duration <= 600 and all(not overlaps(d, (end_time, end_time + duration)) for d in day):
            return n2t(end_time)

    return None

