# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # reach node at position "left"
        left_prev, cur = dummy, head
        for i in range(left - 1):
            left_prev = left_prev.next
            cur = cur.next
        # Now cur = left and leftPrev = node before left
        prev = None
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # Update pointers
        left_prev.next.next = cur
        left_prev.next = prev
        return dummy.next
        
        
        
            
        
        
        
        
        