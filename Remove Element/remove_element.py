from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [num for num in nums if num != val]
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


# 포인터
# python에서 immutable 객체(int, float, str, tuple - 수정 불가능한 객체)에 새로운 값이 할당될 때, 새로운 메모리 공간에 값이 할당된다.
# 즉, 다른 함수에서 값을 변경시에 참조되지 않은 상태로 새로운 매모리에 할당되므로 python Reference count에 의해 메모리에서 삭제될 확률이 크다.
# mutable(list, dict - 수정 가능한 객체) 객체의 값은 기존 메모리를 사용하며 변경이 가능하다. ex) list[:] = new_list
# 단, 새로운 값을 할당시에는 새로운 메모리가 할당됨. ex) list = new_list

# ** reference count: 참조하는 객체의 개수
# sys.getrefcount(객체): reference count 개수 체크
# if reference count == 0 -> 삭제 대상이 되며 메모리 할당 해제

