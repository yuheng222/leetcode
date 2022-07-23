# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        def end_of_first_half(head):
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        if not head:
            return True
        
        first_part_end = end_of_first_half(head)
        second_half_start = reverse_list(first_part_end.next)
        
        result = True
        first_pos = head
        second_pos = second_half_start
        while result and second_pos:
            if first_pos.val != second_pos.val:
                result = False
            first_pos = first_pos.next
            second_pos = second_pos.next
        first_part_end.next = reverse_list(second_half_start)
        return result