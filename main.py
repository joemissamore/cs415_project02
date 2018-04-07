from karat import karat
from exponentiation import exponentation
from printInOrder import printInOrder
from ridOfZeros import ridOfZeros

def main():

    """
    The program should prompt users for integers A and B and then present three options: Task 1, Task 2, Quit.
    Until the user selects Quit, the program should repeatedly prompt these three options.
    """
    message = 'Please select from one of these three options.\n'
    message += 'To calculate the product of A * B enter \"1\"\n'
    message += 'To calculate the power of A raised to B enter \"2\"\n'
    message += 'To quit enter \"3\"\n'
    # message += '\nEnter: '

    a = int(input("Enter a value for A: "))
    b = int(input("Enter a value for B: "))
    print(message)

    while True:
        c = input('\nEnter: ')
        # print(c)
        if c == 1:
            x = karat(a,b)
            x = ridOfZeros(x)
            printInOrder(x)

        elif c == 2:
            x = exponentation(a,b)
            x = ridOfZeros(x)
            printInOrder(x)

        elif c == 3:
            print('Exiting...')
            break
        else:
            print('\nYou have entered an invalid value.\n')

main()
