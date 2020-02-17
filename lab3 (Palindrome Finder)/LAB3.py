#Lab #3
#Due Date: 09/13/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement: 
#
########################################


def removePunctuation(txt):
    value = 0
    statement = list(txt)
    while value < len(txt):
        alpha = statement[value].isalpha()
        if alpha == True:
            value += 1
        else:
            statement[value] = ""
            value += 1
    txt = "".join(statement) 
    return(txt)      

def isPalindrome(text):
    """
        >>> isPalindrome("alula")
        True
        >>> isPalindrome("love")
        False
        >>> isPalindrome("Madam")
        True
        >>> isPalindrome(12.5)
        False
        >>> isPalindrome(12.21)
        False
        >>> isPalindrome("Cigar? Toss it in a can.! It is so tragic.")
        True
        >>> isPalindrome("travel.. a town in Alaska")
        False
    """
    # --- YOU CODE STARTS HERE
    if not isinstance(text, str):
        return False

    new_text = removePunctuation(text)

    rev_list = new_text[::-1] # Found on educative.io
    

    for i in range(0, len(new_text)):
        if new_text[i].lower() != rev_list[i].lower(): #Found .lower() function on GeeksforGeeks.org
            return False
        return True
