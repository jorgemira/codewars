"""
Codewars 4 kyu kata: k-Primes
URL: https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/python
"""


"""
Write function count_Kprimes (or countKprimes or count-K-primes) which given parameters k, start, end (or nd) returns an
 array of the k-primes between start (inclusive) and end (inclusive).
Example:

countKprimes(5, 500, 600) --> [500, 520, 552, 567, 588, 592, 594]
Given positive integers s and a, b, c where a is 1-prime, b 3-prime, c 7-prime find the number of solutions of a + b + c
= s. Call this function puzzle(s).
Example:

puzzle(138) --> 1 ([2 + 8 + 128] is solution)
puzzle(143) --> 2 ([3 + 12 + 128, 7 + 8 + 128] are solutions)
"""


def k_prime(n):
    try:
        return k_prime.cache[n]
    except AttributeError:
        k_prime.cache = {}
    except KeyError:
        pass

    tmp = n
    result = 0
    i = 2

    while tmp > 1:
        if tmp in k_prime.cache:
            result += k_prime.cache[tmp]
            break
        elif i > tmp ** .5:
            result += 1
            break
        elif tmp % i:
            i += 1
        else:
            result += 1
            tmp /= i

    k_prime.cache[n] = result

    return result


def count_Kprimes(k, start, end):
    return [n for n in xrange(start, end + 1) if k_prime(n) == k]


def puzzle(s):
    result = 0
    a_kprimes = []
    b_kprimes = set()
    c_kprimes = []

    for n in xrange(2, s):
        kp = k_prime(n)
        if kp == 1:
            a_kprimes.append(n)
        elif kp == 3:
            b_kprimes.add(n)
        elif kp == 7:
            c_kprimes.append(n)

    for c in c_kprimes:
        for a in a_kprimes:
            if c + a >= s:
                break
            elif s - c - a in b_kprimes:
                result += 1

    return result

