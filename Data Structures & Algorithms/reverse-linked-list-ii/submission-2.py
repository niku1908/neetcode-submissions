# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def solve(self, head, number):

        count = 0

        prev, next = None, None
        temp = head

        while temp:

            next = temp.next
            temp.next = prev
            prev = temp
            temp = next


            if count==number:
                return head, prev, next

            count+=1

        return head, prev, next


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_prev, right_next = None, None
        count = 1
        temp = head


        new_head, prev, next= None, None, None

        if left ==1:
            new_head, prev, next = self.solve(head, right-left)
            new_head.next = next
            return prev

        else:


            while temp:
                
                if count==left-1:
                    left_prev = temp
                    new_head, prev, next = self.solve(temp.next, right-left)
                    # print(new_head.val, prev.val, next.val)
                    break

                temp = temp.next
                count+=1

            

        left_prev.next = prev
        new_head.next = next

        return head