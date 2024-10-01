# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        k = len(lists)
        heap = []

        # Initialize the heap with the head nodes of each list
        for i in range(k):
            if lists[i]:  # Only add non-null nodes
                heapq.heappush(heap, (lists[i].val, i))
        
        dummy = ListNode(-1)
        current = dummy
        
        while heap:
            num, ind = heapq.heappop(heap)
            current.next = ListNode(num)  # Add the smallest value to the merged list
            current = current.next
            
            # Move to the next node in the list from which we extracted the value
            lists[ind] = lists[ind].next
            if lists[ind]:  # If there's a next node, push it to the heap
                heapq.heappush(heap, (lists[ind].val, ind))

        return dummy.next
