from typing import List


class Solution:
    def fill(self, image: List[List[int]], color: int, init_value: int, sr: int, sc: int):
        if image[sr][sc] != init_value:
            return

        image[sr][sc] = color

        if sr > 0:
            self.fill(image, color, init_value, sr - 1, sc)
        if sc > 0:
            self.fill(image, color, init_value, sr, sc - 1)
        if sr < len(image) - 1:
            self.fill(image, color, init_value, sr + 1, sc)
        if sc < len(image[0]) - 1:
            self.fill(image, color, init_value, sr, sc + 1)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.fill(image, color, image[sr][sc], sr, sc)

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
