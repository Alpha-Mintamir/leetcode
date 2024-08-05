class Solution(object):
    def reverseWords(self, s):
        result = []
        s = s.split()
        for i in s:
            result.append(i[::-1])
        return " ".join(result)

        