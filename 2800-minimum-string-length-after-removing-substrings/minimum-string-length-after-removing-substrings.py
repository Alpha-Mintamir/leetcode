class Solution:
    def minLength(self, s: str) -> int:
        strings_to_remove = ["AB","CD" ]
        while "AB" in s or "CD" in s:
            if "AB" in s:

                s = s.replace("AB", '')
            elif "CD" in s:
                s = s.replace("CD", '')
        return len(s)



        