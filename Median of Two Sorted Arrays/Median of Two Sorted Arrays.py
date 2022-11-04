from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(list(nums1 + nums2))
        mid = len(merged_list) // 2

        if len(merged_list) % 2 != 0:
            return float(merged_list[mid])
        else:
            return (merged_list[mid] + merged_list[mid - 1]) / 2
