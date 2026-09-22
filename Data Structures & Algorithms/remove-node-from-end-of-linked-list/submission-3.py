# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        size = 0

        while current:
            size += 1
            current = current.next

        target = size - n

        # The target is the head
        if target == 0:
            return head.next

        current = head

        # Move to the node immediately before the target
        for _ in range(target - 1):
            current = current.next

        current.next = current.next.next

        return head
    




        