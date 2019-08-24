def deep_reverse(L):
    """
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """

    L.reverse()

    for i in L:
        i.reverse()

    print(L)

deep_reverse([[1], [9,5,7], [2,6], [1,5,3,6,8,7]])