class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        is_negative = (dividend < 0) ^ (divisor < 0)

        n = abs(dividend)
        d = abs(divisor)
        quotient = 0

        while n >= d:
            temp_d = d
            multiple = 1
            while n >= (temp_d << 1):
                temp_d <<= 1
                multiple <<= 1

            n -= temp_d
            quotient += multiple
        if is_negative:
            quotient = -quotient
        return min(max(INT_MIN, quotient), INT_MAX)