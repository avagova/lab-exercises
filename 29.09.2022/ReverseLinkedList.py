# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
root = None
def rec(node):
        if node == None:
            print(node,'df')
            root = None
        elif node.next == None:
            global root
            root = node
            return node
        else:
            last = rec(node.next)
            last.next = node
            node.next = None
            return node
class Solution(object):
    def reverseList(self, head):
        rec(head)
        return root
        
