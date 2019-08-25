def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    count = 0
    newHand = hand.copy()
    for i in word:
        if i in newHand.keys() and newHand[i] > 0:
            count += 1
            newHand[i] -= 1
    if count == len(word) and word in wordList:
        return True
    else:
        return False