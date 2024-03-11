class Solution(object):
    def isPowerOfTwo(self, n):


        if n<=0:
            return False
        while n>0:
            if n==1:
                return True
            elif n%2==0:
                n/=2
            else:
                return False
