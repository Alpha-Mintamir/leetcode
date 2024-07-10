class Solution(object):
    def missingNumber(self, nums):
        if not nums:
            return 0
        maximum = max(nums)
        minimum = min(nums)
        
        full_range = set(range(minimum, maximum + 1))
        
        nums_set = set(nums)
        missing_number = full_range - nums_set
        
        if missing_number:
            return missing_number.pop()
        
        
        if minimum > 0:
            return minimum - 1
        else:
            return maximum + 1