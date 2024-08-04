class Solution(object):
    def areOccurrencesEqual(self, s):
        dictt = {}
        for string in s:
            if string in dictt:
                dictt[string] += 1
            else:
                dictt[string] = 1
        values = dictt.values()
        values = set(values)

        if len(values) == 1:
            return True
        else:
            return False
        