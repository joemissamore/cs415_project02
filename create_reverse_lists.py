def create_reverse_lists(a, b):
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
    return LA, LB
