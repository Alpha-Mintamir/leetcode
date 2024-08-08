class Solution(object):
    def hammingWeight(self, n):
        count = 0
        n = bin(n)
        n = str(n)
        for num in n:
            if num == "1":
                count +=1
        return count
