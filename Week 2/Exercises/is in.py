def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if len(aStr) == 1:
        return char == aStr
    elif aStr != '':
        lower = 0
        upper = len(aStr) - 1
        testChar = aStr[round((lower + upper) / 2)]

        if char == testChar:
            return True
        elif char < testChar:
            return isIn(char, aStr[:aStr.index(testChar) + 1])
        elif char > testChar:
            return isIn(char, aStr[aStr.index(testChar) + 1:])
    else:
        return False