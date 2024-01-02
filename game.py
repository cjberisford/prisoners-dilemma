from player import chris

GAME_ROUNDS = 5

p1_score = 0
p2_score = 0
p1_hist = []
p2_hist = []

for n in range(GAME_ROUNDS):
    p1_choice = chris(p1_hist, p2_hist, n)
    p2_choice = True

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

    p1_hist.append(p1_choice)
    p2_hist.append(p2_choice)

print(f'Player 1: {p1_score} Player 2: {p2_score}')
