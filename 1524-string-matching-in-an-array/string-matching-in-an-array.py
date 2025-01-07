class Solution(object):
    def stringMatching(self, words):
        arr = ' '.join(words)
        subStr = [i for i in words if arr.count(i) >= 2]
        
        return subStr
        
        