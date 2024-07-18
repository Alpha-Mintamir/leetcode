class Solution(object):
    def divide(self, dividend, divisor):
        if abs(divisor) == 1:
            dividend = divisor * dividend
            if dividend > 2**31 - 1:
                return 2**31 - 1

            if dividend < -2**31:
                return -2**31

            return dividend

        quotient = 0
        sign = 1
        if dividend * divisor < 0:
            sign = -1

        if dividend < 0: dividend = -dividend
        if divisor < 0: divisor = -divisor

        i = 1
        sum_all = 0
        while sum_all <= dividend:
            if dividend - sum_all < divisor * i:
                i = 1
            quotient += i
            sum_all += divisor * i
            i += 1

        return (quotient - 1) * sign

        