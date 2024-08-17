class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        brokenLetters = set(brokenLetters)
        count = 0
        
        for word in words:
            if not any(letter in brokenLetters for letter in word):
                count += 1
                
        return count
