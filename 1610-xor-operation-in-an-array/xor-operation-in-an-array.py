class Solution(object):
    def xorOperation(self, n, start):
        result = 0
        nums = []
        if n is 1:
            return start
        for i in range(n):
            nums.append(start + 2 * i)
        for num in nums:
            result = result ^ num
        return result 



        
        