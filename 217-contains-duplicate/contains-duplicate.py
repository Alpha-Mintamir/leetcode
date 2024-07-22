class Solution(object):
    def containsDuplicate(self, nums):
        result = set()
        for num in nums:
            if num in result:
                return True
            else:
                result.add(num)
        return False
        