"""
Codewars 5 kyu kata: Bowling score calculator
URL: https://www.codewars.com/kata/5427db696f30afd74b0006a3/python
"""


def bowling_score(rolls):
    score = 0

    for _ in xrange(10):
        frame = rolls.pop(0)
        if frame == 10: # strike
            score += frame + sum(rolls[:2])
        else:
            frame += rolls.pop(0)
            score += frame
            if frame == 10: # spare
                score += rolls[0]
                    
    return score

        
    

def bowling_score(rolls):
    frame, score = 0, 0

    for _ in xrange(10):
        frame = rolls.pop(0)
        if frame == 10: # strike
            score += frame + sum(rolls[:2])
        else:
            frame += rolls.pop(0)
            score += frame
            if frame == 10: # spare
                score += rolls[0]
                    
    return score

        
    

def bowling_score(rolls):
    "Compute the total score for a player's game of bowling."
    frames = []
    new_frame = True

    for i, p in enumerate(rolls):        
        if new_frame:
            if len(frames) == 10:
                break
            frames.append(p)
            if p == 10: # Strike
                frames[-1] += rolls[i+1] + rolls[i+2]
            else:
                new_frame = False
        else:
            frames[-1] += p
            if frames[-1] == 10: # Spare
                frames[-1] += rolls[i+1]
            new_frame = True      

    return sum(frames)

