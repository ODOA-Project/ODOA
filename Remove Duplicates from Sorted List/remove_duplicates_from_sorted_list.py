from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            # 현재 node val와 다음 node val이 같으면
            if node.next and node.val == node.next.val:
                # node next next 를 node next로 끌어 올림
                node.next = node.next.next
            # val이 같지 않으면 node를 한 단계 뒤로.
            else:
                node = node.next
        return head


if __name__ == '__main__':
    head = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1, next=None)))
    answer = Solution.deleteDuplicates(head)
