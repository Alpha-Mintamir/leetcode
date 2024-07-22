class Solution(object):
    def findErrorNums(self, nums):
        result = {}
        duplicate = -1
        missing = -1
        for num in nums:
            if num in result:
                duplicate = num
            result[num] = 1
        for i in range(1, len(nums) + 1):
            if i not in nums:
                missing = i
        return [duplicate, missing]

            



        