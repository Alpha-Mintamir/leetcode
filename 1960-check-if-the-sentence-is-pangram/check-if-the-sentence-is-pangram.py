class Solution(object):
    def checkIfPangram(self, sentence):
        pangram = set(sentence)
        alphabet = set("abcdefghijklmnopqrstuvwxyz")

        return alphabet.issubset(pangram)
        