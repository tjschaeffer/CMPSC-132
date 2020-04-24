#Lab #6
#Due Date: 10/04/2019, 11:59PM 
########################################
#                                      
# Name: 
# Collaboration Statement:           
#
########################################


## ALL FUNCTIONS MUST BE RECURSIVE IN ORDER TO GET CREDIT FOR THEM


def mulBy(num):
    '''
        >>> mulBy(5)
        15
        >>> mulBy(8)
        384
        >>> mulBy(0)
        0
        >>> mulBy(1)
        1
    '''
    # --- Your code starts here
    # Base Case
    if num < 0:
        return 'Error'
    elif num <= 2:
        return num
    # Driver Code
    else:
        return num*(mulBy(num -2))





def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    # --- Your code starts here
    # Base case
    if aList == []:
        return aList
    #Driver code
    if isinstance(aList[0], list):
        return flat(aList[0]) + flat(aList[1:])
    return aList[:1] + flat(aList[1:])





def isPrime(num, i = 2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
    '''
    # --- Your code starts here
    # Base case
    if num < 0:
        return 'Error'
    if (num <= 2):
        if(num == 2):
            return True 
        else:
            return False

    # Driver Code
    if (num % i == 0): 
        return False
    if (i**2 > num): 
        return True
    return isPrime(num, i + 1) 





def countPrimes(num):  # Got help from Ian on this
    '''
        >>> countPrimes(0)
        0
        >>> countPrimes(6)
        3
        >>> countPrimes(2)
        1
        >>> countPrimes(60)
        17
        >>> countPrimes(100)
        25
        >>> countPrimes(500)
        95
    '''
    # --- Your code starts here

    #Base cases
    if num == 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1

    # Driver function
    if isPrime(num):
        return 1 + countPrimes(num - 1)
    else:
        return countPrimes(num - 1)


