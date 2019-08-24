def f(a, b):

    return a > b

def dict_interdiff(d1, d2):
    '''
    Here are two examples:
    If f(a, b) returns a + b
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    If f(a, b) returns a > b
    d1 = {1:30, 2:20, 3:30}
    d2 = {1:40, 2:50, 3:60}
    then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

    '''


    intersect = {}
    difference = {}

    for key1 in d1.keys():
        for key2 in d2.keys():
            if key1 == key2:
                intersect[key1] = f(d1[key1], d2[key2])
            elif key1 not in d2.keys():
                difference[key1] = f(d1[key1], )
            elif key2 not in d1.keys():
                difference[key2] = f(d2[key2], )


    return print((intersect, difference))

dict_interdiff({1:30, 2:20, 3:30, 5:80}, {1:40, 2:50, 3:60, 4:70, 6:90})