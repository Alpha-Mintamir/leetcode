class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        result = {}
        for i in range(len(nums)):
            if (nums[i] in result):
                j = result[nums[i]]
                if(abs(i - j) <=k):
                    return True
            result[nums[i]] = i
        return False
        