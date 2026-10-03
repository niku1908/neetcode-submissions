"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def combine(self, head, new_head):

        t1 = head
        t2 = new_head

        while(t1 and t2):
            next = t1.next
            t1.next = t2
            t2= next
            t1 = t1.next
        return head

    def make_random(self, head):

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            if temp.next:
                temp = temp.next.next

    def separate_head(self, head):
        
        t1 = head
        t2 = head.next
        new_head = t2

        while(t1 and t2):

            t1.next = t2.next
            t1 = t2.next
            if t1:
                t2.next = t1.next
            
                t2 = t1.next

        return new_head
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        new_head, tail = None, None
        temp = head
        while(temp):
            new_node = Node(temp.val)
            if new_head is None:
                new_head = new_node
            if tail is None:
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            temp = temp.next

        self.combine(head, new_head)

        self.make_random(head)

        new_head = self.separate_head(head)
        return new_head

            