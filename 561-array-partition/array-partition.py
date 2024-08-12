class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort() 
        left, right = 0, 1
        total = 0
        while right < len(nums):
            total += nums[left]  
            left += 2
            right += 2
        return total
