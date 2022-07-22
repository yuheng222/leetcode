# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cycle_length = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                current = slow
                while True:
                    current = current.next
                    cycle_length += 1
                    if current == slow:
                        break
                p1, p2 = head, head
                for i in range(cycle_length):
                    p2 = p2.next
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None
                