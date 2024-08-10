class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictt = {}
        for num in nums:
            dictt[num] = dictt.get(num, 0)+1
        for i, j in dictt.items():
            if j > len(nums)/2:
                return i
        
        