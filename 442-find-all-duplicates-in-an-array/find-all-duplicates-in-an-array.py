class Solution(object):
    def findDuplicates(self, nums):
        hashmap = {}
        result = []

        for num in nums:
            if num in hashmap:
                result.append(num)
            hashmap[num] = 1
        return result

                
        