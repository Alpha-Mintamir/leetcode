class Solution(object):
    def heightChecker(self, heights):
        count = 0
        sorted_height = list(sorted(heights))
        for i, j in zip(heights, sorted_height):
            if i != j:
                count += 1
        return count
        