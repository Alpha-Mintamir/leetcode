class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {"2":'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'}
        digits = list(digits)
        result = []
        if digits == "":
            return []
        if len(digits) == 1:
            return num_to_letter[digits[0]]
        elif len(digits) == 2:
            for i in num_to_letter[digits[0]]:
                for j in num_to_letter[digits[1]]:
                    result.append(''.join([i,j]))
            return result
        elif len(digits) == 3:
            for i in num_to_letter[digits[0]]:
                for j in num_to_letter[digits[1]]:
                    for k in num_to_letter[digits[2]]:

                        result.append(''.join([i,j,k]))
            return result
        elif len(digits) == 4:
            for i in num_to_letter[digits[0]]:
                for j in num_to_letter[digits[1]]:
                    for k in num_to_letter[digits[2]]:
                        for l in num_to_letter[digits[3]]:
                            result.append(''.join([i,j,k,l]))
            return result





        