class Solution:
    def maxScore(self, s: str) -> int:
        maxx = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            left_count = left.count('0')
            right_count = right.count('1')

            maxx = max(maxx, left_count+ right_count)

            
        return maxx
            
        