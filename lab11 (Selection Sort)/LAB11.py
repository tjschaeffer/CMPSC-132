#LAB 11
#Due Date: 11/22/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:        
#
########################################


def selectionSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of selection sort
        2nd returned value: the sorted list

        >>> selectionSort([9,3,5,4,1,78,67])
        ({1: [9, 3, 5, 4, 1, 78, 67], 2: [1, 3, 5, 4, 9, 78, 67], 3: [1, 3, 5, 4, 9, 78, 67], 4: [1, 3, 4, 5, 9, 78, 67], 5: [1, 3, 4, 5, 9, 78, 67], 6: [1, 3, 4, 5, 9, 78, 67], 7: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
    '''
    # YOUR CODE STARTS HERE

    dic = {}
    length = len(numList)
    key = 0
    for i in range(length):
    	key = key + 1
    	newList = numList[:]
    	dic.update({key: newList})
    	item = i
    	for index in range(item, length):
    		if numList[item] > numList[index]:
    			item = index
    	numList[i], numList[item]= numList[item], numList[i]
    return dic, numList
