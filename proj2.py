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
    :param a: (list)
    :param b: (list)
    :return: a*b
    '''
    if len(a) == 1 and len(b) == 1:
        return a[0] * b[0]
    if (len(a) > len(b)):
        b = b + [0] * (len(a) - len(b))
    if (len(b) > len(a)):
        a = a + [0] * (len(b) - len(a))
    ka = len(a) // 2
    kb = len(b) //2
    A2 = a[:ka]
    A1 = a[ka:]
    B2 = b[:kb]
    B1 = b[kb:]
    #print("A1", A1)
    #print("A2",A2)
    #print("B1",B1)
    #print("B2",B2)
    a1b1 = karat(A1,B1)
    #print(a1b1)
    a12b12 = karat((add(A1,A2)),(add(B1,B2)))
    #print(a12b12)
    a2b2 = karat(A2,B2)
    #print(a2b2)
    k = max(ka,kb)
    return (a1b1 * (10 ** (2*k))) + (((a12b12) - a1b1 - a2b2)* (10 ** k)) + a2b2
    #return 0
def main():
    a = int(input("Enter a value for A:"))
    b = int(input("Enter a value for B:"))
    LA = []
    LB = []
    #appends integer in reverse order
    while a > 0:
        LA.append(a%10)
        a = a//10
    while b > 0:
        LB.append(b%10)
        b= b//10
    #adds extra 0's to make lists the same size
    if(len(LA) > len(LB)):
        LB =LB + [0] * (len(LA)-len(LB))
    if (len(LB) > len(LA)):
        LA =LA + [0] * (len(LB) - len(LA))

    value = karat(LA,LB)
    print(value)

main()
