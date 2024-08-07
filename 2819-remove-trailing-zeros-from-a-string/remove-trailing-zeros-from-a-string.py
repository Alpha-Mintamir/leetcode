class Solution(object):
    def removeTrailingZeros(self, num):
        last = len(num)
        for i in range(len(num) - 1, -1, -1):
            if num[i] == "0":
                last -= 1
            else:
                break
        return num[:last]