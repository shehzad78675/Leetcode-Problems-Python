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

        
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        dummy = ListNode(-1)
        tem = dummy
        
        while heap:
            num, ind = heapq.heappop(heap)
           
            lists[ind] = lists[ind].next
            if lists[ind]:
                heapq.heappush(heap, (lists[ind].val, ind))
            
            tem.next = ListNode(num)
            tem = tem.next

        return dummy.next
