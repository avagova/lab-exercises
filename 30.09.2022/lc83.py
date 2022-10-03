# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        l = head
        while head != None:
            if head.val != l.val:
                l.next = head
                l = head
            head = head.next
        if l != None:
            l.next = None
        return root
