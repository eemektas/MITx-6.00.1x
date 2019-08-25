def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    lenght = 0
    for i in hand.keys():
        lenght += hand[i]
    return lenght
