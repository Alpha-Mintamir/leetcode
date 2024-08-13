class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        result = []
        for word in words:
            result.extend([subword for subword in word.split(separator) if subword])

        return result
