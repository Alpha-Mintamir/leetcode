class Solution(object):
    def majorityElement(self, nums):
        majority_num = len(nums) / 2
        dictt = {}

        for i in nums:
            if i in dictt:
                dictt[i] += 1
            else:
                dictt[i] = 1
        for key, value in dictt.items():
            if value > majority_num:
                return key