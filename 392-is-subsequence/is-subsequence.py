class Solution(object):
    def isSubsequence(self, s, t):
        it = iter(t)
        return all(char in it for char in s)
