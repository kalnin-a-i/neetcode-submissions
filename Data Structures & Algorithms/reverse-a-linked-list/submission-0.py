# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        elif not head.next.next:
            first = head
            second = head.next
            first.next, second.next = None, first
            return second
        
        prev = head
        cur_node = head.next
        next_node = head.next.next
        prev.next = None
        while next_node:
            cur_node.next = prev
            prev, cur_node, next_node = cur_node, next_node, next_node.next
        cur_node.next = prev
        return cur_node
            
            