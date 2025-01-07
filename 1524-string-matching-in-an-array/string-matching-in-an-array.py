class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        length = len(words)
        for word in range(length):
            for i in range(length):
                if i == word:
                    continue
                if words[word] in words[i]:
                    result.append(words[word])
                    break
        return result


        