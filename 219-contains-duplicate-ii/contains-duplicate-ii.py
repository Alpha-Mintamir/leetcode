class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        result = {}
        for i, num in enumerate(nums):
            if num in result:
                if abs(result[num]-i) <= k:
                    return True
            result[num] = i
        return False
        