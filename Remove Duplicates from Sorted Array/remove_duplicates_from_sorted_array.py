class Solution(object):
    def removeDuplicates(self, nums) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)
