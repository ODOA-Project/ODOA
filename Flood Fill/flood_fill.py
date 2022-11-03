from typing import List


class Solution:
    def __init__(self):
        self.image: List[List[int]] = []
        self.color: int = 0
        self.value: int = 0  # 시작 픽셀 값

    def fill(self, sr: int, sc: int):
        if self.image[sr][sc] != self.value:
            return

        self.image[sr][sc] = self.color

        if sr > 0:
            self.fill(sr - 1, sc)
        if sc > 0:
            self.fill(sr, sc - 1)
        if sr < len(self.image) - 1:
            self.fill(sr + 1, sc)
        if sc < len(self.image[0]) - 1:
            self.fill(sr, sc + 1)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.image = image
            self.color = color
            self.value = image[sr][sc]
            self.fill(sr, sc)

        return image


if __name__ == "__main__":
    cases = [
        {
            "image": [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            "sr": 1,
            "sc": 1,
            "color": 2,
            "result": [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        },
        {
            "image": [[0, 0, 0], [0, 0, 0]],
            "sr": 0,
            "sc": 0,
            "color": 0,
            "result": [[0, 0, 0], [0, 0, 0]]
        }
    ]

    for case in cases:
        result = Solution().floodFill(case["image"], case["sr"], case["sc"], case["color"])
        print("result", result)
        assert result == case["result"]
