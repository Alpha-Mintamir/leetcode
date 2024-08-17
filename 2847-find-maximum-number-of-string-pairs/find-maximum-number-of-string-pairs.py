class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        count = 0
        dictt = {}

        for i in words:
            dictt[''.join(sorted(i))] = dictt.get(''.join(sorted(i)), 0) + 1
        for i in dictt.values():
            if i == 2:
                count += 1
        return count
        