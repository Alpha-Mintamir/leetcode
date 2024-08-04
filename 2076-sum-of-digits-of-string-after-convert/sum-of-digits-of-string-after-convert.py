class Solution(object):
    def getLucky(self, s, k):
        result = [ord(char.lower()) - ord('a') + 1 for char in s]
        result = ''.join(str(num) for num in result)
        for _ in range(k):
            total = sum(int(digit) for digit in result)
            result = str(total)
        
        return int(result)