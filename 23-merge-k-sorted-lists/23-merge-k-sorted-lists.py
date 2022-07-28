from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx))
        head = curr = ListNode(0)
        while heap:
            val, idx = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heappush(heap, (lists[idx].val, idx))
        return head.next