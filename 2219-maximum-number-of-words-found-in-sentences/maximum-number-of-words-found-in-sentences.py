class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0
        maxx = count
        for i in sentences:
            count = len(i.split())
            maxx = max(maxx, count)
        return maxx
            
        