class Solution(object):
    def finalValueAfterOperations(self, operations):
        val = {"X--": -1, "--X": -1, "++X": 1, "X++":1}
        result = []
        for operation in operations:
            result.append(val[operation])
        return sum(result)
                
        