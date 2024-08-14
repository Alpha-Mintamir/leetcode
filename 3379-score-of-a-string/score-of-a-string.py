class Solution(object):
    def scoreOfString(self, s):
        total_score = 0
        for i in range(len(s) - 1):
            total_score += abs(ord(s[i]) - ord(s[i + 1]))
        return total_score
