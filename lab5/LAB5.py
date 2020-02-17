#Lab #5
#Due Date: 09/27/2019, 11:59PM EST
########################################
#                                      
# Name:
# Collaboration Statement:          
#
########################################

class Complex:
    '''
        >>> a=Complex(5,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7, 8i)
        >>> a-b
        (3, -20i)
        >>> a*b
        (94, 58i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> print(a)
        5-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5, 6i)
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
    '''
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    # --- YOU CODE STARTS HERE
    def __add__(self, other): # Addition
        return Complex(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other): # Subtraction 
        return Complex(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other): # Multiplication
        return Complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __rmul__(self, other): # Supports reverse multiplication 
        return self.__mul__(other)
    def __str__(self): # Gives string representation
        return str(int(self.real))+('+' if self.imag>=0 else '-')+str(int(abs(self.imag)))+'i' # Got help w/ternary operators from Ian
    def __repr__(self): # Got help on this from Ian; direct representation
        return f'({self.real}, {self.imag}i)'
    @property    
    def conjugate(self): # Finding conjugate
        return Complex(self.real, (-1*self.imag))
    def __eq__(self, other): # Boolean operator 
        return str(self) == str(other)