class Solution(object):
    def searchRange(self, nums, target):
        def indexFromTheLeft(nums, target):
            left, right = 0, len(nums)-1
            index = -1
            while(left <= right):
                mid = (left + right)//2
                if(nums[mid]== target):
                    index = mid
                    right = mid -1

                elif(nums[mid]<target):
                    left = mid + 1
                elif(nums[mid]>target):
                    right = mid - 1
            return index
        def indexFromTheRight(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        result = [indexFromTheLeft(nums, target), indexFromTheRight(nums, target)]
        return result
    
        
        