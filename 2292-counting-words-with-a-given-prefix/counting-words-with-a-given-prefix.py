class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        summ = 0
        for word in words:
            if word[:len(pref)] == pref:
                summ += 1
        return summ
        