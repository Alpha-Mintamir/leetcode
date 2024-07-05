class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        letter_count = {}
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        for letter2 in ransomNote:
            if letter2 in letter_count and letter_count[letter2] > 0:
                letter_count[letter2] -= 1
            else:
                return False
        
        return True


