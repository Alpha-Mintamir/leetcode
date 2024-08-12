class Solution(object):
    def maximumWealth(self, accounts):
        summ = 0
        for i in accounts:
            summ = max(summ, sum(i))
        return summ
        