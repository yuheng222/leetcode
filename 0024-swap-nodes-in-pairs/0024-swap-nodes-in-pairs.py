# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save the pointer to the next pair and the "current" head
            nxt_pair = curr.next.next
            second = curr.next
            # swap the nodes
            second.next = curr
            curr.next = nxt_pair
            prev.next = second
            # increment the pointers
            prev = curr
            curr = nxt_pair
        return dummy.next            