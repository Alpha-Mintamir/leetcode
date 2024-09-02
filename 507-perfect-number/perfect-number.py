import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        result = set()
        for i in range(1, int(math.sqrt(num)) +1):
            if num%i == 0:
                result.add(i)
                result.add(num//i)
        result = list(result)
        result = sorted(result)
        result = result[:-1]
        if sum(list(result)) == num:
            return True
        else:
            return False

        