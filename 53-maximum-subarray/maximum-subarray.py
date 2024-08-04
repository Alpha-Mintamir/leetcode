class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = current_sum 
         
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

        