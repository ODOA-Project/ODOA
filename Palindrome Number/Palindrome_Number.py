class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x) == str(x)[::-1]
