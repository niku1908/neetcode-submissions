# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = list1
        temp2 = list2
        if not temp1:
            return temp2

        if not temp2:
            return temp1

        next, prev = None, None
        head = None

        while(temp1 and temp2):
            if temp1.val<=temp2.val:
                if head is None:
                    head = temp1
                if prev is None:
                    prev = temp1
                else:
                    prev.next = temp1
                    prev = temp1

                temp1 = temp1.next


            else:
                if head is None:
                    head = temp2
                if prev is None:
                    prev = temp2
                else:
                    prev.next = temp2
                    prev = temp2

                temp2 = temp2.next

        if temp2:
            prev.next = temp2
        if temp1:
            prev.next = temp1
                
  
        return head


