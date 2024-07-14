class Solution(object):
    def searchRange(self, nums, target):
        def findStartingIndex(nums, target):
            index = -1
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
                if nums[mid] == target:
                    index = mid
            return index
        
        def findEndingIndex(nums, target):
            index = -1
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
                if nums[mid] == target:
                    index = mid
            return index
        
        start = findStartingIndex(nums, target)
        end = findEndingIndex(nums, target)
        
        return [start, end]
        
        