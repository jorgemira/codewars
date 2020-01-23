"""
Codewars 6 kyu kata: Instant Runoff Voting
URL: https://www.codewars.com/kata/52996b5c99fdcb5f20000004/python
"""


def runoff(voters):
    while voters:
        parties = {}
        for voter in voters:
            for i, v in enumerate(voter):
                parties[v] = parties.get(v, 0) + (0 if i else 1)

        winner, votes = max(((k, v) for k, v in parties.iteritems()), key=lambda x: x[1])
        if votes > len(voters) / 2:
            return winner
        min_votes = min(v for v in parties.values())
        min_parties = [k for k, v in parties.iteritems() if v == min_votes]
        voters = [list(filter(lambda x: x not in min_parties, v)) for v in voters]
        voters = [v for v in voters if len(v)]

    return None

