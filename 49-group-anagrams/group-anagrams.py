from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        anagramGroup = defaultdict(list)

        for s in strs:
            sorted_str = tuple(sorted(s))
            anagramGroup[sorted_str].append(s)

        for i in anagramGroup.values():
            result.append(i)
        return result
        