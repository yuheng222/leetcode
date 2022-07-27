from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, element in enumerate(lists):
            if element:
                heappush(heap,(element.val, idx))
        head = curr = ListNode(0) # set head and curr to a dummy node
        while heap:
            val, idx = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx].next: # if there is another node in the linked list
                lists[idx] = lists[idx].next # set the first node as the next node
                heappush(heap, (lists[idx].val, idx)) # push the next node of the linked list into the heap
        return head.next # return the initial head pointer