def lessThan4(aList):
    '''
    Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters.
    For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]
    This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
    '''

    bList = []

    for value in aList:

        if len(value) < 4:
            bList.append(value)

    return bList

print(lessThan4(["b", "apple", "cat", "dog", "banana"]))