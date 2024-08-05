class Solution(object):
    def reverseStr(self, s, k):
        result = []
        s = [s[i:i+k] for i in range(0, len(s), k)]
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(s[i][::-1])
            else:
                result.append(s[i])
        return ''.join(result)