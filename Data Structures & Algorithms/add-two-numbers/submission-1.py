# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur_node = head
        remain = 0
        while l1 and l2:
            new_node = ListNode()
            cur_node.next = new_node
            cur_node = new_node

            digit = (l1.val + l2.val + remain) % 10
            remain = (l1.val + l2.val + remain) // 10
            cur_node.val = digit
            l1 = l1.next
            l2 = l2.next
        print(remain)
        print(cur_node.val)
        if l1:
            cur_node.next = l1
        elif l2:
            cur_node.next = l2
        elif remain > 0:
            cur_node.next = ListNode(val=remain)
            return head.next 
        else:
            return head.next 
        
        # cur_node = cur_node.next
        while cur_node.next:
            cur_node = cur_node.next
            cur_node.val, remain = (cur_node.val + remain) % 10, (cur_node.val + remain) // 10
            
        
        if remain > 0:
            cur_node.next = ListNode(val=remain)

        return head.next
