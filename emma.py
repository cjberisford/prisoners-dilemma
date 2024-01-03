#Co-operate or defect
import random

def emma(my_choice_hist, their_choice_hist, current_round_number):

    weighting = 0.5
    for response in their_choice_hist:
        if current_round_number == 0:
            pass
        elif response == True:
            weighting *= 1.05
        else:
            weighting *= 0.75

    weighting = min (weighting, 0.99)

    if random.random() <= weighting:
        return True
    else:
        return False
    
# #Test data
# p1_dummy_history = [True, True, True, True]
# p2_dummy_history = [True, True, True, True]
# emma(p1_dummy_history, p2_dummy_history, 3)