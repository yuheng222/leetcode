# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(cur, prev):
            if cur is None:
                return prev
            nxt = cur.next
            cur.next = prev
            return reverse(nxt, cur)
        return reverse(head, None)