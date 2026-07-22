class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        digit_sum = 0

        while n > 0:
            digit = n % 10
            if digit != 0:
                x = str(digit) + x
                digit_sum += digit
            n //= 10

        if x == "":
            return 0

        return int(x) * digit_sum