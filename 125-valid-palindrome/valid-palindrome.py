class Solution(object):
    def isPalindrome(self, s):
        k = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                k = k + i
        return k == k[::-1]

        