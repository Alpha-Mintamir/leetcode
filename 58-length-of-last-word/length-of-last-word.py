class Solution(object):
    def lengthOfLastWord(self, s):
        list1 = s.split()
        n = len(list1)
        return len(list1[n-1])
        