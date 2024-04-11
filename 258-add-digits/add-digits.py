class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            num = digit_sum
        return num

            
        