# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head
        head = root 
        while head and head.next :
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return root.next
