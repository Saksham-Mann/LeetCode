# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=headA
        l2=headB
        l12=0
        l21=0
        while l1!=l2:
            if not l1:
                if l12==0:
                    l1=headB
                    l12=1
                else:
                    return None
            else:
                l1=l1.next
            if not l2:
                if l21==0:
                    l2=headA
                    l21=1
                else:
                    return None
            else:
                l2=l2.next
        return l1
