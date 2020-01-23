"""
Codewars 6 kyu kata: Find the divisors!
URL: https://www.codewars.com/kata/544aed4c4a30184e960010f4/python
"""


from math import sqrt

def divisors(num):
    divs = []
    
    for i in xrange(2, int(sqrt(num) + 1)):
        if not num % i:
            divs.append(i)
            if i != num/i:
                divs.append(num/i)
    
    return sorted(divs) if divs else "%i is prime" % num

