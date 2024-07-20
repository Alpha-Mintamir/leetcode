class Solution(object):
    def isHappy(self, n, seen=None):
        if seen is None:
            seen = set()

        if n == 1:
            return True

        if n in seen:
            return False
        seen.add(n)

        n = sum(int(digit) ** 2 for digit in str(n))


        return self.isHappy(n, seen)





        