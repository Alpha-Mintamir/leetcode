class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] + nums[j]
                if k == target:
                    output = [i, j]


        return output

        