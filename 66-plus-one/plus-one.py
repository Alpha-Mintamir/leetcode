class Solution(object):
    def plusOne(self, digits):
        strings = ''.join(str(i) for i in digits)
        incremented = int(strings) + 1
        result = (int(digit) for digit in str(incremented))
        return result

            

        