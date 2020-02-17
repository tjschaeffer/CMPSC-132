import unittest 
from LAB3 import * 


class PalindromeTestCases(unittest.TestCase):
    """Tests for LAB3.py"""
    def test_for_words(self):
        """Is the word a palindrome?"""
        self.assertTrue(isPalindrome('alula'))
        self.assertFalse(isPalindrome(42))
        self.assertFalse(isPalindrome('$$$'))

    def test_for_lowercase(self):
        """Is the word a palindrome that is lowercase?"""
        self.assertFalse(isPalindrome('RACETRACK'))
        self.assertTrue(isPalindrome('racecar'))
        self.assertTrue(isPalindrome('anna'))

    def test_for_mixed_letters(self):
        """Is the word a palindrome with upper and lower case letters?"""
        self.assertTrue(isPalindrome('DeWeD'))
        self.assertFalse(isPalindrome('reNert'))
        self.assertFalse(isPalindrome('HANGER'))
 

    def test_for_strings_w_punctuations(self):
        """Is the string with punctuation a palindrome?"""
        self.assertTrue(isPalindrome('Dammit, I’m mad!'))
        self.assertTrue(isPalindrome('Did I cite Operas Are Poetic? I did.'))
        self.assertFalse(isPalindrome('Who went home last week?'))

    def test_for_spaces(self):
      	"""Is the string with spaces a palindrome?"""
      	self.assertTrue(isPalindrome(' Dial Laid '))
      	self.assertFalse(isPalindrome('Hello there stranger'))
      	self.assertFalse(isPalindrome('17 38'))

    def test_for_uppercase(self):
        """Is the word a palindrome with uppercase letters?"""
        self.assertFalse(isPalindrome('turner'))
        self.assertFalse(isPalindrome('retrospect'))
        self.assertTrue(isPalindrome('DUMB MUD'))











#Do not modify the 2 lines below
if __name__ == '__main__':
	unittest.main(exit=False)