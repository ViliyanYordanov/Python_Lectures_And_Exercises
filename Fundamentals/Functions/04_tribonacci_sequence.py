# def tribonacci_sequence(num):
#     for index in range(1, num + 1):
#
#
#
# number = int(input())
# tribonacci_sequence(number)


def printTribRec(n):
    if (n == 3):
        return 1
    else:
        return (printTribRec(n - 1) +
                printTribRec(n - 2) +
                printTribRec(n - 3))


def printTrib(n):
    for i in range(1, n):
        print(printTribRec(i), " ", end="")


# Driver code
n = int(input())
printTrib(n)
