from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive_nums = list(sorted(set([num for num in nums if num > 0])))
        if not positive_nums:
            return 1

        if len(positive_nums) == positive_nums[-1]:
            return positive_nums[-1] + 1

        diff_nums = [i for i, num in enumerate(positive_nums) if i + 1 != num]
        return diff_nums[0] + 1
        # left = 0
        # right = positive_nums_len - 1
        # middle = (left + right) // 2
        # middle_value = positive_nums[middle]
        # while left < right:
        #     if middle + 1 == middle_value:
        #         left = middle + 1
        #     elif middle + 1 < middle_value:
        #         right = middle
        #     else:
        #         return middle
        #     middle = (left + right) // 2
        #     middle_value = positive_nums[middle]
        # return middle + 1


if __name__ == "__main__":
    cases = [
        {
            "nums": [3, 4, -1, 1],
            "result": 2
        },
        {
            "nums": [7, 8, 9, 11, 12],
            "result": 1
        }
    ]

    for case in cases:
        result = Solution().firstMissingPositive(case["nums"])
        print("result", result)
        assert result == case["result"]
