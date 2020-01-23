"""
Codewars 6 kyu kata: validDate Regex
URL: https://www.codewars.com/kata/548db0bd1df5bbf29b0000b7/python
"""


import re
valid_date = re.compile("""\[(
                        ((0[13578]|1[02])-(0[1-9]|[12]\d|3[01]))| # 31 days
                        ((0[469]|11)-(0[1-9]|[12]\d|30))|         # 30 days
                        (02-(0[1-9]|1\d|2[0-8]))                  # 28 days
                        )\]""", re.X)

