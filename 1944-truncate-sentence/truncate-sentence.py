class Solution(object):
    def truncateSentence(self, s, k):
        s = s.split()
        s = s[:k]
        return " ".join(s)
        