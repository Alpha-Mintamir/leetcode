class Solution(object):
    def sumBase(self, n, k):
        if n == 0:
            return "0"

        digits = []
        while n:
            digits.append(int(n % k))
            n //= k
        return sum(digits)

        