class Solution(object):
    def numOfPairs(self, nums, target):
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        return count
