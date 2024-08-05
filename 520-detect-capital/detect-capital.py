class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper():
            return True
        if word[0].islower():
            return word.islower()
        elif word[0].isupper() and word[1:].islower():
            return True
        