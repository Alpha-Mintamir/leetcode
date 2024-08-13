class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            index = word.index(ch)
            rev = ''.join(reversed(word[:index+1]))
            return ''.join([rev, word[index+1:]])
        else:
            print("Character not found in word.")
            
            return word
        