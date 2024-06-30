class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        result1 = []
        result2 = []
        final_result = []
        for i in nums1:
            if (i in nums2):
                result1.append(i)
        for j in nums2:
            if (j in nums1):
                result2.append(j)
        num_result1 = len(result1)
        num_result2 = len(result2)
        final_result.append(num_result1)
        final_result.append(num_result2)
        return final_result

        