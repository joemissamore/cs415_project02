"""
    Karat
"""
from add import add
from subtract import subtract
from power import power
from create_reverse_lists import create_reverse_lists

def karat(a, b):
    '''
    Implementation of the
    :param a: (int) or list reverse order
    :param b: (int) or list reverse order
    :return: a reversed list of the product a * b
    '''
    if (type(a) == int):
        a, b = create_reverse_lists(a, b)
    if len(a) == 1 and len(b) == 1:
        d,e = create_reverse_lists(a[0]*b[0], 0)
        return d
    if (len(a) > len(b)):
        b = b + [0] * (len(a) - len(b))
    if (len(b) > len(a)):
        a = a + [0] * (len(b) - len(a))
    k = len(a) // 2

    A2 = a[:k]
    A1 = a[k:]
    B2 = b[:k]
    B1 = b[k:]

    a1b1 = karat(A1, B1)
    a12b12 = karat((add(A1, A2)), (add(B1, B2)))
    a2b2 = karat(A2, B2)
    # print(a12b12)
    # print('k: ' + str(k) + '\n')
    # print ('a1b1: ' + str(a1b1))
    stepone = power(a1b1, 2 * k)
    # print('stepone: ' + str(stepone) + '\n')
    # stepone = (a1b1 * (10 ** (2 * k)))

    # print ('a12b12: ' + str(a12b12))
    steptwo = subtract(a12b12,a1b1)
    # print('steptwo: ' + str(steptwo) + '\n')
    # steptwo = (a12b12) - a1b1

    # print ('a2b2: ' + str(a2b2))
    stepthree = subtract(steptwo,a2b2)
    # print('stepthree: ' + str(stepthree) + '\n')
    # stepthree = steptwo - a2b2


    stepfour = power(stepthree,k)
    # print('stepfour: ' + str(stepfour))
    # stepfour = (10 ** k)

    stepfive = add(stepone,stepfour)
    # print('stepfive: ' + str(stepfive))

    stepsix = add(stepfive,a2b2)
    # print('stepsix: ' + str(stepsix))

    return stepsix
