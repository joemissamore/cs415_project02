def subtract(L1, L2):
    """
    Input: 2 lists in reverse order
    Output: 1 list with subtraction

    The function assumes L1 - L2
    Example usage:
    # L1 = 34580293458
    # L2 = 45023475
    # L1, L2 = create_reverse_lists(L1, L2)
    # L1, L2 = initLists(L1, L2)
    #
    # L = subtract(L1, L2)
    #
    # printInorder(L)
    """
    a = L1
    b = L2

    minLen = min(len(L1), len(L2))

    L = []
    for i in range(minLen):
        m = a[i] - b[i]
        if m < 0:
            a[i+1] = a[i+1] - 1
            a[i] += 10
            m = a[i] - b[i]
        L.append(m)

    return L
