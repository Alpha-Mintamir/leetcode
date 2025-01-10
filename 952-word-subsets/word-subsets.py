from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_counts = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_counts[char] = max(max_counts[char], word_count[char])
        
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_counts[char] for char in max_counts):
                result.append(word)
        
        return result
