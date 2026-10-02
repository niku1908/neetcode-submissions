# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mapping = {}
        if not head.next:
            return 

        temp = head
        i = 0
        while(temp):
            mapping[i]=temp
            i+=1
            next = temp.next
            temp.next = None
            temp = next

        length = i

        count = 0
        new_head, tail = None,None
        while(count!=length//2):
            node1 = mapping[count]
            node2 = mapping[length-count-1]
            if new_head is None:
                new_head = node1
            node1.next = node2
            count+=1
            if tail is None:
                tail = node2
            else:
                tail.next = node1
                tail = node2

        if length%2!=0:
            tail.next = mapping[(length//2)]
        # return new_head




        