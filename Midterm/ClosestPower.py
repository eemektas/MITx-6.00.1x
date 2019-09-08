def closest_power(base, num):
    '''
    :param base: base of the exponential, integer > 1
    :param num: number you want to be closest to, integer > 0
    :return: the exponent
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    '''

    exponent = 0
    result = 0

    while True:

        result = base ** exponent

        if result == num or base ** (exponent + 1) > num:
            if num - result == base ** (exponent + 1) - num:
                return exponent
            elif num - result > base ** (exponent + 1) - num:
                return exponent + 1
            else:
                return exponent

        else:
            exponent += 1


print(closest_power(5, 27))
print(closest_power(5, 75))
print(closest_power(5, 76))
print(closest_power(5, 1))