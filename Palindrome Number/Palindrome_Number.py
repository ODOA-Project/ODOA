from math import log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x) == str(x)[::-1]


class LogarithmSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 < x < 10:
            return True

        digit_count = 1 + int(log10(x))
        half = int(digit_count / 2)
        digits = list(map(lambda exp: int(x / pow(10, exp) % 10), range(digit_count)))
        left = digits[:half]
        digits.reverse()
        right = digits[:half]
        return all(map(lambda y: y[0] == y[-1], zip(left, right)))
