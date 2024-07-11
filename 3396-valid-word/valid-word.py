class Solution(object):
    def isValid(self, word):
        vowel = set("aeiouAEIOU")
        vowel_count = 0
        consonant_count = 0

        if len(word) < 3 or not word.isalnum():
            return False

        for char in word:
            if char.isalpha():
                if char in vowel:
                    vowel_count += 1
                else:
                    consonant_count += 1

        return vowel_count > 0 and consonant_count > 0
