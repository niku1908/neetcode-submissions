# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def get_num(self, l1):

        string = ""
        temp = l1
        while temp:
            string+=f"{temp.val}"
            temp = temp.next
        string = string[::-1]
        return int(string)

    def get_head(self, num):

        string = str(num)
        string = string[::-1]
        head, tail = None, None
        for i in string:
            new_node = ListNode(int(i))
            if head is None:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = tail.next

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)

        result = num1+num2
        head = self.get_head(result)
        return head