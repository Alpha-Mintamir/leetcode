class Solution(object):
    def findWords(self, words):
        result = []
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        for word in words:
            lower_case = word.lower()
            if all(char in first_row for char in lower_case):
                result.append(word)
            elif all(char in second_row for char in lower_case):
                result.append(word)
            elif all(char in third_row for char in lower_case):
                result.append(word)
        return result
            



        words = "".join(sorted(words))

        
        