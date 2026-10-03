# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l = 0
        temp = head
        while(temp):
            l+=1
            temp = temp.next

        count = 0
        target = l-n
        if target==0:
            return head.next
        temp = head
        while(temp):
            count+=1
            if count==target:
                if temp.next:
                    next = temp.next.next
                temp.next = next
                break
            temp = temp.next
        return head

