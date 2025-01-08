class Solution(object):
    def countPrefixSuffixPairs(self, words):
        total_len = len(words)
        result = 0
        for word in range(total_len):
            for i in range(word+1, total_len):
                length = len(words[word])
                if word == i:
                    continue
                else:
                    if words[i][0: length] == words[word] and words[i][-length:] == words[word]:
                        result += 1
        return result


            
        