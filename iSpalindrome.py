class Solution(object):
    def isPalindrome(self, x):

        #turn the given number into string
      
        numX = str(x)

        #compare the reversed version of the given number with the original given number
        if numX[::-1] == str(x):
            return True

      #if they are the same, we return True (It's a palindrome)

        else:
            False

      #else, we return False (It isn't a palindrome)

#By Mehdi Khoudali, Leetcode challenge
