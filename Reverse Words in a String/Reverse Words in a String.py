class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(lambda c: c, reversed(s.split(" "))))


if __name__ == '__main__':
    r = Solution().reverseWords("blue is the sky")
    print(r)
