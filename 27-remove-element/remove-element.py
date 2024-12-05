class Solution(object):
    def removeElement(self, nums, val):
        t = 0  
        for num in nums:
            if num != val:
                nums[t] = num
                t += 1
        
        return t
