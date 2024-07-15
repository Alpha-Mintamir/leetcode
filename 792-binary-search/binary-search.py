class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if(nums[mid] == target):
                return mid
            elif(nums[mid]<target):
                left = mid + 1
            elif(nums[mid]>target):
                right = mid -1
        return -1

        