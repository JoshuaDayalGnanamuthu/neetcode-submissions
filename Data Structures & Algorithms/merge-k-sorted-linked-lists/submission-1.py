# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = []

        for head in lists:
            current = head
            while current:
                sorted_list.append(current.val)
                current = current.next
        
        if not sorted_list:
            return None

        sorted_list.sort()

        head = ListNode(sorted_list[0])
        previous = head

        for i in range(1, len(sorted_list)):
            new_node = ListNode(sorted_list[i])
            previous.next = new_node
            previous = new_node
        
        return head


