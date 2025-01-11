class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i,j in zip(word1, word2):
            result.append(i)
            result.append(j)
        if len(word1) > len(word2):
            result.append(word1[len(word2):])
        else:
            result.append(word2[len(word1):])
        return ''.join(result)

        