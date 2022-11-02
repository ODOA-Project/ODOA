class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) ** 2 == num

if __name__ == "__main__":
    _input = 16
    result = Solution().isPerfectSquare(_input)

    assert result == True
