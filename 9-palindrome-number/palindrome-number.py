class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        k = x[::-1]
        
        if k == x:
            return True
        else:
            return False

        