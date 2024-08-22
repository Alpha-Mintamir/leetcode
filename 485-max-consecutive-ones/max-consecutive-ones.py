class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            max_count = max(max_count, right - left + 1)
        
        return max_count
