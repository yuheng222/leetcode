# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        cur, prev = head, None
        # move the two pointers until they start at the proper starting point in the list
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1
        
        # two pointers that will fix the final connections
        tail, con = cur, prev
        
        # reverse the needed nodes
        while right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            right -= 1
        
        # Adjust final connections, check if con is null or not. if it is null. set head as prev directly
        if con:
            con.next = prev
        else:
            head = prev
        # connect tail of reversed nodes to right subnodes
        tail.next = cur
        return head
            
        
        
        
        
        