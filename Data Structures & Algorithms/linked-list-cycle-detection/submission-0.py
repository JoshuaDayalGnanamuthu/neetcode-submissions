# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        current = head
        if not current:
            return False

        while (current.next):
            if current not in seen:
                seen.add(current)
                current = current.next
            else:
                return True
        
        return False
