# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        count=1
        oddHead=None
        evenHead=None
        oddTail=None
        evenTail=None
        current=head
        while current:
            if count&1==0:
                if not evenHead:
                    evenHead=evenTail=current
                else:
                    evenTail.next=current
                    evenTail=evenTail.next
            else:
                if not oddHead:
                    oddHead=oddTail=current
                else:
                    oddTail.next=current
                    oddTail=oddTail.next
            count+=1
            current=current.next
        if not evenHead:
            return oddHead
        if not oddHead:
            return evenHead
        oddTail.next=evenHead
        evenTail.next=None
        return oddHead