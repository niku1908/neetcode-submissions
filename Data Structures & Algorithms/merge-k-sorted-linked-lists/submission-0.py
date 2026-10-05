# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr= []
        for i in lists:
            temp = i
            while(temp):
                arr.append((temp.val, temp))
                next = temp.next
                temp.next = None
                temp = next

        arr.sort(key=lambda item: item[0])

        head, tail = None, None
        for i in arr:
            new_node = i[1]
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        return head