class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_length = min(len(s) for s in strs)

        prefix = ""

        for i in range(min_length):

            current_char = strs[0][i]


            for s in strs:
                if s[i] != current_char:
                    return prefix


            prefix += current_char

        return prefix


