def ridOfZeros(L):
    """
    Input: A reverse list
    Returns: A list without unnecessary trailing zeros

    If input is an artibrary list of all zeros
    Will return [0]

    """
    for i in range(len(L) - 1, 0, -1):
        if L[i] == 0:
            del L[i]
        else:
            break

    if len(L) == 0:
        L = [0]

    return L
