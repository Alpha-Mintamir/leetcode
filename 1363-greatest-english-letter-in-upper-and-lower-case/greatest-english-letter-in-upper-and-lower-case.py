class Solution(object):
    def greatestLetter(self, s):
        result = []
        for i in s:
            t = i.lower()
            if i.isupper() and t in s:
                result.append(i)
        if result:

            result = set(result)
            return max(result)
        else:
            return ''
        