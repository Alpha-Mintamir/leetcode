class Solution:
    def checkString(self, s: str) -> bool:
        sorted_s = sorted(s)
        sorted_s = ''.join(sorted_s)
        if s == sorted_s:
            return True
        else:
            return False
