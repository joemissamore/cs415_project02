from karat import karat

def exponentation(a, b):
    """
    Input: Two integers
    Returns: a reversed list of integers
    """
    prev_b_even = []
    orig_a = [a]

    while b != 1:
        if b % 2 == 1:
            prev_b_even.append(False)
            b = (b - 1) / 2

        else:
            prev_b_even.append(True)
            b = b / 2

    for i in reversed(prev_b_even):
        if i == False:
            a = karat(a, a)
            a = karat(a, orig_a)
        else:
            a = karat(a, a)

    return a



# printInorder(exponentation(5, 20))
# print (karat(2, 15))
