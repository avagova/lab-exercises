# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l1, l2):
    i = l1
    j = l2
    res = ListNode(0)
    cur = res
    while l1 and l2:
        cur.next = ListNode(0)
        cur = cur.next
        if l1.value <= l2.value:
            cur.value = l1.value
            l1 = l1.next
        else:
            cur.value = l2.value
            l2 = l2.next
    while l1:
        cur.next = ListNode(0)
        cur = cur.next
        cur.value = l1.value
        l1 = l1.next
    while l2:
        cur.next = ListNode(0)
        cur = cur.next
        cur.value = l2.value
        l2 = l2.next
    return res.next
            
