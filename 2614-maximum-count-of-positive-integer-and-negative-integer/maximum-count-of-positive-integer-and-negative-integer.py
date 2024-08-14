class Solution(object):
    def maximumCount(self, nums):
        count_positive = 0
        count_negative = 0
        for i in nums:
            if i>0:
                count_positive += 1
            elif i<0:
                count_negative += 1
        return max(count_positive, count_negative)


        