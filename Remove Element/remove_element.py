from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

if __name__ == "__main__":
    _nums = [0,1,2,2,3,0,4,2]
    _val = 2
    expected_nums = [0, 0, 1, 3, 4]

    result = Solution().removeElement(_nums, _val)

    assert result == len(expected_nums)
    _nums.sort()
    for idx in range(len(_nums)):
        assert _nums[idx] == expected_nums[idx]


