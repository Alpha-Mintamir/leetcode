class Solution(object):
    def firstUniqChar(self, s):
        reslut = {}
        count = 1
        for i in s:
            if i in reslut:
                reslut[i] +=1
            else:
                reslut[i] = 1
        for k, first_char in enumerate(s):
            if reslut[first_char] == 1:
                return k
        return -1

        