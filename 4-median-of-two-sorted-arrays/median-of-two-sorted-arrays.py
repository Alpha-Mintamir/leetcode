class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result = list(sorted(nums1 + nums2))
        n = len(result)
        half = n//2
        if n % 2 == 0:
            return (result[half] + result[half-1])/2.0
        else:
            return result[half]
        