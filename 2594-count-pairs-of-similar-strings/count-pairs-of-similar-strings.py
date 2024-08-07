class Solution(object):
    def similarPairs(self, words):

        char_sets = [tuple(sorted(set(word))) for word in words]
    
        # Count the number of similar pairs
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if char_sets[i] == char_sets[j]:
                    count += 1
        
        return count
                    
        