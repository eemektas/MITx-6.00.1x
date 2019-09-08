def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    lower = min(a, b)

    while a % lower != 0 or b % lower != 0:
        lower -= 1

    return lower