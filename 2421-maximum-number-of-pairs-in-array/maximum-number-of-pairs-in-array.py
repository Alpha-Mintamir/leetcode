class Solution(object):
    def numberOfPairs(self, nums):
        pairs = 0
        leftovers = 0
        dictt = {}
        for i in nums:
            dictt[i] = dictt.get(i, 0)+1
        
        for i in dictt.values():
            if i%2 != 0:
                leftovers += 1
                pairs += i//2

            else:
                pairs += i//2
        return [pairs, leftovers]



        