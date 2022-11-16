from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for str_v in strs:
            for i, c in enumerate(prefix):
                if len(str_v) - 1 < i or str_v[i] != c:
                    prefix = prefix[:i]
                    break
        return prefix


if __name__ == "__main__":
    cases = [
        {
            "strs": ["flower", "flow", "flight"],
            "result": "fl"
        },
        {
            "strs": ["dog", "racecar", "car"],
            "result": ""
        }
    ]

    for case in cases:
        result = Solution().longestCommonPrefix(case["strs"])
        print("result", result)
        assert result == case["result"]
