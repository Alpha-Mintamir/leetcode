class Solution(object):
    def containsDuplicate(self, nums):
        result = {}
        for num in nums:
            if num in result:
                return True
            else:
                result[num] = num
        return False
        