#HW #1
#Due Date: 09/20/2019, 11:59PM 
########################################
#                                      
# Name: TJ Schaeffer
# Collaboration Statement: Got help from LAs            
#
########################################



def isPower(x, y):
    """
        >>> isPower(4, 64)
        3
        >>> isPower(5, 81)
        -1
        >>> isPower(7, 16807)
        5
    """
    # --- YOU CODE STARTS HERE
    exp = 0 
    power = 1
    while (abs(power) < abs(y)): 
        power = power * x
        exp +=1 
    if power == y: #If power is equal to y
        return exp
    else:
        return -1



def translate(translationDict, txt):
    """
        >>> myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1': 'one'} 
        >>> text = 'Up down left Right forward 1 time' 
        >>> translate(myDict, text) 
        'down up right left forward one time'
    """
    # --- YOU CODE STARTS HERE
    output = [] # Blank list for translation
    lower_txt = txt.lower() # Turn all letters into lowercase
    lst = str.split(lower_txt) # Turn txt into list to iterate

    for word in lst:
        if word in translationDict:
            translated_word = translationDict[word] 
            output.append(translated_word)
        else:
             output.append(word)
    space = ' '
    string = space.join(output)
    return string





def onlyTwo(x, y, z):
    """
        >>> onlyTwo(1, 2, 3)
        13
        >>> onlyTwo(3, 3, 2)
        18
        >>> onlyTwo(5, 5, 5)
        50
    """
    # --- YOU CODE STARTS HERE
    first = max(x, y)
    second = max(y,z)
    if first == second:
        second = max(x, z)
    return first**2 + second**2




def largeFactor(num):
    """
        >>> largeFactor(15) 
        5
        >>> largeFactor(24)
        12
        >>> largeFactor(7)
        1
    """
    # --- YOU CODE STARTS HERE
    factors = []
    for f in range(1, num):
        if num % f == 0: # If remainder is equal to zero
            factors.append(f) # Add that number to list
            largestF = factors[-1] # Select largest factor
    return largestF




def hailstone(num):
    """
        >>> hailstone(5)
        [5, 16, 8, 4, 2, 1]
        >>> hailstone(6)
        [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    # --- YOU CODE STARTS HERE
    newList = []
    newList.append(num) # Add starter number to list
    while num > 1:
        if num % 2 != 0:
            num = (num * 3) + 1
        else:
            num /= 2
        newList.append(int(num)) # Adding new number
    return newList