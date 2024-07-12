class Solution(object):
    def runningSum(self, nums):
        summ = 0
        result = []
        for num in nums:
            summ += num
            result.append(summ)
        return result

        