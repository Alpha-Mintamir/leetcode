class Solution(object):
    def letterCombinations(self, digits):
        
        combinations = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        if len(digits) == 0:
            return result
        elif len(digits) == 1:
            for i in combinations[digits]:
                result.append(i)
        elif len(digits) == 2:
            for i in combinations[digits[0]]:
                for j in combinations[digits[1]]:
                    result.append(''.join([i,j]))
        elif len(digits) == 3:
            for i in combinations[digits[0]]:
                for j in combinations[digits[1]]:
                    for k in combinations[digits[2]]:
                        result.append(''.join([i,j,k]))
        else:
            for i in combinations[digits[0]]:
                for j in combinations[digits[1]]:
                    for k in combinations[digits[2]]:
                        for l in combinations[digits[3]]:
                            result.append(''.join([i,j,k,l]))
        return result


