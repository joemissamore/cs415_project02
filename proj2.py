"""
    Proj 2
"""
def add(a,b):
    """
    :param a: (list)
    :param b: (list)
    :return: c(list) - (a+b)
    """
    c = []
    remainder = 0
    r = min(len(a), len(b))

    for i in range(r):
        value = a[i] + b[i] + remainder
        if value >=10:
            c.append(value%10)
            remainder = value//10
        else:
            c.append(value)
    if(len(a) > len(b)):
        value = a[len(a)-1] + remainder
        if value >=10:
            c.append(value%10)
            remainder = value//10
        else:
            c.append(value)
    if (len(b) > len(a)):
        value = b[len(b) - 1] + remainder
        if value >= 10:
            c.append(value % 10)
            remainder = value // 10
        else:
            c.append(value)
    if(remainder != 0):
        c.append(1)
    return c


def karat(a,b):
    '''
    Implementation of the
    :param a: (int) or list reverse order
    :param b: (int) or list reverse order
    :return: a*b
    '''
    if(type(a) == int):
        a,b = create_reverse_lists(a,b)
    if len(a) == 1 and len(b) == 1:
        return a[0] * b[0]
    if (len(a) > len(b)):
        b = b + [0] * (len(a) - len(b))
    if (len(b) > len(a)):
        a = a + [0] * (len(b) - len(a))
    k = len(a) // 2

    A2 = a[:k]
    A1 = a[k:]
    B2 = b[:k]
    B1 = b[k:]

    a1b1 = karat(A1,B1)
    a12b12 = karat((add(A1,A2)),(add(B1,B2)))
    a2b2 = karat(A2,B2)
    return (a1b1 * (10 ** (2*k))) + (((a12b12) - a1b1 - a2b2)* (10 ** k)) + a2b2

def create_reverse_lists(a,b):
    LA = []
    LB = []
    # appends integer in reverse order
    while a > 0:
        LA.append(a % 10)
        a = a // 10
    while b > 0:
        LB.append(b % 10)
        b = b // 10
    # adds extra 0's to make lists the same size
    if (len(LA) > len(LB)):
        LB = LB + [0] * (len(LA) - len(LB))
    if (len(LB) > len(LA)):
        LA = LA + [0] * (len(LB) - len(LA))
    return LA,LB

def main():
    a = int(input("Enter a value for A:"))
    b = int(input("Enter a value for B:"))
    value = karat(a,b)
    print(value)

main()
