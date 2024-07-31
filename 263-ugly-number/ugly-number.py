class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        else:
            for factor in[2,3,5]:
                while n % factor ==0:
                    n //= factor
            return n == 1
        