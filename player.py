"""return true or false depending on action"""


def chris(p1_hist, p2_hist, round):
    print(p1_hist, p2_hist, round)
    prev_round_choice = True
    if round >= 1:
        prev_round_choice = p2_hist[round-1]
    return not prev_round_choice


test_p1_hist = [True, True, False]
test_p2_hist = [True, True, True]

# print(chris(test_p1_hist, test_p2_hist, 1))
