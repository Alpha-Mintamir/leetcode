class Solution(object):
    def maxFrequencyElements(self, nums):
        dictt = {}
        result1 = []
        for i in nums:
            dictt[i] = dictt.get(i, 0)+1

        result = dictt.values()
        for i in result:
            if i == max(result):
                result1.append(i)
        return sum(result1)

        