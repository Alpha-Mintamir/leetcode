

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_elements = sorted(set(nums))  
        if len(distinct_elements) >= 3:
            return distinct_elements[-3]  
        else:
            return max(distinct_elements) 
