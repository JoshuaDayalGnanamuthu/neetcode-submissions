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
                heapq.heappush(heap, (head.val, index, head)) # put the heads of all the linked lists in a min heap. This gaurentess that the head with the smallest val is at the start of the heap. The tuple's first arg is the head val, the heap will compare based on this. The second arg is the index of the list from 0 to k. this is beacuse if we have two of the same values, the heap will go on to compare the next ele. As heads are not compareable, we pass index of each tuple before that, which is gaurentted to be unique per tuple.

        if not len(heap):
            return None
        
        _, index, head = heapq.heappop(heap)
        if head.next:
            next_node = head.next
            heapq.heappush(heap, (next_node.val, index, next_node))
        
        current = head
        while len(heap):
            _, index, min_node = heapq.heappop(heap)

            current.next = min_node
            current = min_node

            if min_node.next:
                next_node = min_node.next
                heapq.heappush(heap,(next_node.val, index, next_node))
        
        return head
        

        



