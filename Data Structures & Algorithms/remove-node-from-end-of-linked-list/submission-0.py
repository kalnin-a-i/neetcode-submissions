# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur_head = head
        while cur_head:
            length += 1
            cur_head = cur_head.next
        
        node_number = length - n + 1
        cur_head = head
        cur_number = 1
        if node_number == 1:
            return head.next
        while cur_head:
            if cur_number == node_number-1:
                cur_head.next = cur_head.next.next
                break
            cur_number += 1
            cur_head = cur_head.next
        return head