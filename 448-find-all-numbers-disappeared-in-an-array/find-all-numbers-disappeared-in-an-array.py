class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        nums.sort()
        newNums = []
        all_nums = set(range(1, n+1))
        for i in nums:
            if(i in all_nums):
                all_nums.remove(i)
        
        newNums = list(all_nums)   
        return newNums    
        