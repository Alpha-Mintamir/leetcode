class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s) - 1

        while left < right:
            if (s[left] in vowel) and (s[right] in vowel):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowel:
                left += 1
            elif s[right] not in vowel:
                right -= 1

        return ''.join(s)
