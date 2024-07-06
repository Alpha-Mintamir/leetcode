class Solution(object):
    def intersect(self, nums1, nums2):
        from collections import Counter
        
        counts = Counter(nums1)
        
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
                
        return result
