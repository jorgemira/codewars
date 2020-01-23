"""
Codewars 6 kyu kata: Catching Car Mileage Numbers
URL: https://www.codewars.com/kata/52c4dd683bfd3b434c000292/python
"""


def is_interesting(number, awesome_phrases):
    checks = [lambda x: not x % 10 ** (len(str(x)) - 1), # 1 digit + 0s
              lambda x: str(x) == str(x)[::-1], # All digits equal & palyndroms
              lambda x: str(x) in "1234567890", # Incrementing       
              lambda x: str(x) in "9876543210", # Decrementing
              lambda x: x in awesome_phrases] # Number in awesome_phrases

    for i, n in enumerate(xrange(number, number + 3)):
        if n > 99 and any(c(n) for c in checks):
            return 1 if i else 2

    return 0

        
    

def is_interesting(number, awesome_phrases):
    
    checks = []
    checks.append(lambda x: str(x) == str(x)[::-1])
    checks.append(lambda x: not x % 10 ** (len(str(x))-1))  
    checks.append(lambda x: str(x) in "1234567890")
    checks.append(lambda x: str(x) in "9876543210")
    
    for i in xrange(number, number + 3):
        if i > 99 and any(c(i) for c in checks) or i in awesome_phrases:
            return 2 if i == number else 1
    
    return 0

