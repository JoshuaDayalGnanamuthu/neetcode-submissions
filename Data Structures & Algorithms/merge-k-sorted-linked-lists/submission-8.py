# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        if not lists:
            return None
        
        heap = []
        
        for index, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, index, head))
        
        if not len(heap):
            return None
            
        _, index, head = heapq.heappop(heap)

        if head.next:
            heapq.heappush(heap, (head.next.val, index, head.next))
        
        current = head
        while len(heap):
            _, index, node = heapq.heappop(heap)
            current.next = node

            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
            
            current = current.next
        
        return head


        

        



