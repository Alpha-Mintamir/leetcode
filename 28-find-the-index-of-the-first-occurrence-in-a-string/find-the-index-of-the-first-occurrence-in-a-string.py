class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        l,r = 0, k-1
        while r < len(haystack):
            if haystack[l:r+1] == needle:
                return l
            else:
                l+=1
                r+=1
        return -1
        