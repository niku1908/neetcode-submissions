# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_ll(self, head, k):

        prev, temp = None, head
        count = 0
        while(count!=k):
            count+=1
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count= 0
        temp = head
        while(temp and count!=k):
            count+=1
            temp = temp.next
            
            
        

        if count<k:
            return head

        new_reverse_head = self.reverse_ll(head, k)
        if temp:
            reverse_head = self.reverseKGroup(temp, k)
            
            head.next = reverse_head
        return new_reverse_head

        

        
        




