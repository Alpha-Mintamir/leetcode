class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def fromLeft(nums, target):
            found = -1
            left, right = 0, len(nums)-1
            while left<=right:
                mid = (left + right)//2
                if nums[mid] == target:
                    found = mid
                    right = mid-1
                elif nums[mid]< target:
                    left = mid+1
                else:
                    right = mid-1
            return found
        def fromRight(nums, target):
            found = -1
            left, right = 0, len(nums)-1
            while left<=right:
                mid = (left + right)//2
                if nums[mid] == target:
                    found = mid
                    left = mid+1
                elif nums[mid]< target:
                    left = mid+1
                else:
                    right = mid-1
            return found
        return([fromLeft(nums, target),fromRight(nums, target)] )            

            
            

        