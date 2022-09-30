# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        a = set()
        while head != None:
            print(head.val,id(head))
            if id(head) in a:
                return True
            a.add(id(head))
            head = head.next
        return False
