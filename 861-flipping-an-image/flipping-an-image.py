class Solution(object):
    def flipAndInvertImage(self, image):
        finalResult = []
        for row in image:
            reversed_row = list(reversed(row))
            inverted_row = [1 - x for x in reversed_row]
            finalResult.append(inverted_row)
        return finalResult