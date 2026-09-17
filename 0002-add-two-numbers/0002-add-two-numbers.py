# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        temp=dummy
        carry=0
        left=l1
        right=l2
        while left and right:
            temp.next=ListNode(0)
            temp=temp.next
            temp.val=(left.val+right.val+carry)%10
            carry=(left.val+right.val+carry)//10
            left=left.next
            right=right.next
        while left:
            temp.next=ListNode(0)
            temp=temp.next
            temp.val=(left.val+carry)%10
            carry=(left.val+carry)//10
            left=left.next
        while right:
            temp.next=ListNode(0)
            temp=temp.next
            temp.val=(right.val+carry)%10
            carry=(right.val+carry)//10
            right=right.next
        if carry!=0:
            temp.next=ListNode(0)
            temp=temp.next
            temp.val=carry
        return dummy.next