#Lab #1
#Due Date: 08/30/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:          
#
########################################


def sumSquares(aList):
    """
        >>> sumSquares(5)
        'error'
        >>> sumSquares('5')
        'error'
        >>> sumSquares(6.15)
        'error'
        >>> sumSquares([1,5,-3,5,9,8,4])
        90
        >>> sumSquares(['3',5,-3,5,9.0,8,4,'Hello'])
        90.0
    """
    if isinstance(aList, list):
        total=0
        for value in aList:
            if(isinstance(value, int) or isinstance(value, float)) and abs(value)%3==0:
               total+=value**2
        return total
    else:
        return 'error'
