"""
Codewars 3 kyu kata: Invalid Login - Bug Fixing #11
URL: https://www.codewars.com/kata/55e4c52ad58df7509c00007e/python
"""


def validate(username, password):
    wrong = ['||', '//']
    for w in wrong:
        if  w in username or w in password:
            return 'Wrong username or password!'
    
    validator = Validator()
    return validator.login(username, password)

