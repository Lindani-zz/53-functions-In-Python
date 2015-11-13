def sum_list(n):
    theSum = 0
    myList = []
    for numbers in range(1, n+1):
        myList.append(numbers)
    for result in myList:
        theSum += result
    return theSum
