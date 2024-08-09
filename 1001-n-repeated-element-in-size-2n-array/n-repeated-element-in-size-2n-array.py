class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        result = {}
        for i in nums:
            result[i] = result.get(i, 0)+1
        for i, j in result.items():
            if j == n:
                return i
        



        