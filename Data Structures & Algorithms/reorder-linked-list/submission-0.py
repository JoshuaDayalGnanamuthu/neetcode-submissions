class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            current = head
            previous = None

            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            return previous

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = reverseList(slow.next)
        slow.next = None

        current = head

        while tail:
            next_node = current.next
            next_tail = tail.next

            current.next = tail
            tail.next = next_node

            current = next_node
            tail = next_tail