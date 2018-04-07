def add(a, b):
    """
    :param a: (list)
    :param b: (list)
    :return: c(list) - (a+b)
    """

    DEBUG = False
    if(len(a) == 0):
        return []
    c = []
    remainder = 0
    if (len(a) > len(b)):
        b = b + [0] * (len(a) - len(b))
    if (len(b) > len(a)):
        a = a + [0] * (len(b) - len(a))
    #r = min(len(a), len(b))
    if DEBUG:
        print ('Printing out a and b after length adjustment...\n')
        print ('a: ' + str(a))
        print ('b: ' + str(b))
        print('\nEnd printing after length adjustment\n')

        print ('Entering value loop...\n')

    # i = 0
    # while i < range(len(a)) or remainer != 0:
    # remainder = 0
    for i in range(len(a)):
        value = a[i] + b[i] + remainder
        if DEBUG:
            print ('Calculating value ...\n')
            print ('i: ' + str(i) + '\n\n')
            print ('a[' + str(i) + ']: ' + str(a[i]))
            print ('b[' + str(i) + ']: ' + str(b[i]))
            print ('value: ' + str(value))
            print ('remainder: ' + str(remainder))
            print ('\nEnd Calculating value ...\n')
        if value >= 10:
            c.append(value % 10)
            remainder = value // 10
            if DEBUG:
                print('Entering value >= 10 ...\n')
                print('c is appending: ' + str(value % 10))
                print ('remainder: ' + str(remainder))
                print ('\nEnd value >= 10\n')
        else:

            c.append(value)
            if DEBUG:
                print ('Entering else statement')
                print ('c is appending: ' + str(value))
                print ('End else statement\n')

        # flush remainder
        if value < 10:
            remainder = 0

    if remainder != 0:
        c.append(remainder)
        if DEBUG:
            print ('\nEntering remainder != 0 ...\n')
            print ('c is appending: ' + str(remainder))
            print ('\nEnd remainer != 0\n')


        # i += 1
    """
    if (len(a) > len(b)):
        value = a[len(a) - 1] + remainder
        if value >= 10:
            c.append(value % 10)
            remainder = value // 10
        else:
            c.append(value)
    if (len(b) > len(a)):
        value = b[len(b) - 1] + remainder
        if value >= 10:
            c.append(value % 10)
            remainder = value // 10
        else:
            c.append(value)
    """
    # if (remainder != 0):
    #     c.append(1)

    return c
