class Solution(object):
    def similarPairs(self, words):
        count = 0
        for i in range(len(words)):
            for j in range(i +1, len(words)):
                if ''.join(list(sorted(list(set(words[i]))))) == ''.join(list(sorted(list(set(words[j]))))):
                    count += 1
        return count
                    
        