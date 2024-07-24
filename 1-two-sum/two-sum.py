class Solution(object):
    def twoSum(self, nums, target):
        dictt = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in dictt:
                return [index, dictt[complement]]
            else:
                dictt[num] = index

