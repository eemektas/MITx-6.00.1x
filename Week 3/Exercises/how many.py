def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0

    for i in aDict.values():
        for j in i:
            count += 1

    return count