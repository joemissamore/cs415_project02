def subtract(a, b):
    """
    :param a: (list)
    :param b: (list)
    :return: c(list) - (a+b)
    """
    if(len(a) == 0):
        return []
    c = []

    if (len(a) > len(b)):
        b = b + [0] * (len(a) - len(b))
    if (len(b) > len(a)):
        a = a + [0] * (len(b) - len(a))

    #print(a)
    #print(b)
    for i in range(len(a)-1):
        if a[i] >= b[i]:
            value = a[i] - b[i]
        else:
            a[i+1] = a[i+1] - 1
            value = (a[i] + 10) - b[i]
        c.append(value)

    value = a[len(a)-1] - b[len(b)-1]
    c.append(value)
    if(len(c)) != 1:
        for i in range(len(c)):
            if(c[len(c)-1]) == 0:
                c = c[:len(c)-1]
            else:
                break
    return c
