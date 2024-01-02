def tit_for_tat(my_choice_history, their_choice_history, current_round_number):
    """
    Determines an action in the Prisoner's Dilemma. This is a simple implementation
    that mimics the other player's previous action. It is also 'friendly', which means
    it always returns True in the first round.

            Parameters:
                    my_choice_history (list): Player 1 previous actions
                    their_choice_history (list): Player 2 previous actions   
                    current_round_number (int): The current round number (0 indexed, so 0 is round 1 etc.)

            Returns:
                    cooperate (boolean): True if action is 'Cooperate', False if action is 'Defect' 
    """
    cooperate = their_choice_history[current_round_number - 1] if current_round_number >= 1 else True
    return cooperate