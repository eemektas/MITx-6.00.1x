def maxVal(t):
    '''
    def max_val(t):
        t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t
    For example,
    max_val((5, (1,2), [[1],[2]])) returns 5.
    max_val((5, (1,2), [[1],[9,5,7]])) returns 9.
    Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
    '''

    assert t == ("") or [""], "t can not be empty"

    nList = []

    for sub in t:
        if type(sub) == int:
            nList.append(sub)
        else:
            for item in sub:
                if type(item) != int:
                    for elem in item:
                        nList.append(elem)
                else:
                    nList.append(item)

    return print(max(nList))

maxVal((5, (1,2), [[1],[9,5,7]]))
