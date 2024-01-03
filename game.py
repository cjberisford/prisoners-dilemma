from chris import tit_for_tat, lucky_seven
from emma import emma

GAME_ROUNDS = 500
p1_score, p2_score = 0, 0
p1_hist, p2_hist = [], []

for n in range(GAME_ROUNDS):
    p1_choice = tit_for_tat(p1_hist, p2_hist, n) 
    p2_choice = emma(p2_hist, p1_hist, n)

    if p1_choice and p2_choice:
        p1_score += 3
        p2_score += 3
    elif not p1_choice and not p2_choice:
        p1_score += 1
        p2_score += 1
    elif p1_choice and not p2_choice:
        p2_score += 5
    elif not p1_choice and p2_choice:
        p1_score += 5

    print(f'P1: {"Cooperates" if p1_choice else "Defects"}, P2: {"Cooperates" if p2_choice else "Defects"}')

    p1_hist.append(p1_choice)
    p2_hist.append(p2_choice)

print("*****************************")
print(f'* P1 Total: {p1_score} P2 Total: {p2_score} *')
print("*****************************")