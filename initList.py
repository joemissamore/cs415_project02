def initLists(L1, L2):
    """
    Input: Two lists in reverse order
    Output: Two lists where one of them is maxSize(L1, L2) - 1 in length

    This fuction gurantees that the lists will be able to be used by
    add and subtract.
    """

    smList = None
    bigListSize = max(len(L1), len(L2))
    smListSize = min(len(L1), len(L2))
    diff = bigListSize - smListSize

    if len(L1) < len(L2):
        smList = L1
        smListName = 'L1'
    elif len(L1) > len(L2):
        smList = L2
        smListName = 'L2'
    else:
        return L1, L2

    L = [0] * (diff - 1)
    L.extend(smList)

    if smListName == 'L1':
        L1 = L
    else:
        L2 = L

    return L1, L2
