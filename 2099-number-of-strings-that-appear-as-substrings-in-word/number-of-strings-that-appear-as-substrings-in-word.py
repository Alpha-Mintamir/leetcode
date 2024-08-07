class Solution(object):
    def numOfStrings(self, patterns, word):
        count = 0
        for i in patterns:
            if i in word:
                count +=1
        return count
        