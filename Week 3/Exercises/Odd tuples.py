def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    newTup = ()
    i = 0

    while i < len(aTup):
        newTup += (aTup[i],)
        i += 2

    return newTup