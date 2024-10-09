class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        results = []
        for i in range(len(number)):
            if number[i] == digit:
                results.append(number[:i] + number[i+1:])
        return max(results)
