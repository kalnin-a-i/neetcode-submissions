"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node(x=head.val)
        cur = new_head
        created = {head : new_head}
        while head:
            # print(head)
            if not head.next in created and  not head.next is None:
                cur.next = Node(x=head.next.val)
                created[head.next] = cur.next
            elif head.next is None:
                cur.next = None
            else:
                cur.next = created[head.next]

            
            if not head.random in created and not head.random is None:
                cur.random = Node(x=head.random.val)
                created[head.random] = cur.random
            elif head.random is None:
                cur.random = None
            else:
                cur.random = created[head.random]

            
            cur = cur.next
            head = head.next

        return new_head