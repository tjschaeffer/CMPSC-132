#Lab #2
#Due Date: 09/06/2019, 11:59PM 
########################################
#                                      
# Name:
# Collaboration Statement:            
#
########################################

def removePunctuation(txt):
    """
        >>> removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        'I like chocolate cake      It s the best flavor      for real'
        >>> removePunctuation("Dots...................... many dots..X")
        'Dots                       many dots  X'
        >>> removePunctuation(55)
        'None'
        >>> removePunctuation([3.5,6]) 
        'None'
    """
    # --- YOU CODE STARTS HERE
    if not isinstance(txt, str):
        return 'None'  

    value = 0
    statement = list(txt)
    while value < len(txt):
        alpha = statement[value].isalpha()
        if alpha == True:
            value += 1
        else:
            statement[value] = " "
            value += 1
        txt = "".join(statement) 
    return(txt)      


def studentGrades(gradeList):
    """
        >>> gradeList = [
        ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
        ...     ['John', 100, 90, 80],
        ...     ['McVay', 88, 99, 111],
        ...     ['Rita', 45, 56, 67],
        ...     ['Ketan', 59, 61, 67],
        ...     ['Saranya', 73, 79, 83],
        ...     ['Min', 89, 97, 101]]
        >>> studentGrades(gradeList)
        [90, 99, 56, 62, 78, 95]
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2'],
        ...     ['John', 100, 90],
        ...     ['McVay', 88, 99],
        ...     ['Min', 89, 97]]
        >>> studentGrades(grades)
        [95, 93, 93]
        >>> studentGrades(55)
        'None'
        >>> studentGrades('32')
        'None'
    """
    # --- YOU CODE STARTS HERE
    try:
        if type(gradeList) == list:
            averagesList = []
            row = 1
            while row < len(gradeList):
                rowSum = sum(gradeList[row][1:])
                rowAverage = rowSum / (len(gradeList[1]) - 1)
                rowAverage = int(rowAverage)
                averagesList.append(rowAverage)
                row += 1
        else:
            averagesList = 'None'
        return(averagesList)
    except:
        return('None')
