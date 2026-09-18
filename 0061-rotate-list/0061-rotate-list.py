# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k==0:
            return head
        tail=head
        length=1
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        tail.next=head
        r=length-k
        for _ in range(r):
            tail=tail.next
        newHead=tail.next
        tail.next=None
        return newHead