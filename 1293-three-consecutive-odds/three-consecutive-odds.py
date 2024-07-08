class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False
