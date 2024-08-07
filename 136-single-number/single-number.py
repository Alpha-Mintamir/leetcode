class Solution(object):
    def singleNumber(self, nums):
        dictt = {}
        for num in nums:

            dictt[num] = dictt.get(num, 0)+1
        for i, j in dictt.items():
            if j ==1:
                return i

    
        
        