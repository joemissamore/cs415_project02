import sys

def printInOrder(L):
    for i in reversed(L):
        sys.stdout.write(str(i))
    sys.stdout.write('\n')
