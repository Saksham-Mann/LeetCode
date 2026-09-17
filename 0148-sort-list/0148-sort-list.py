# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getMid(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(0)
        temp = dummy
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp=temp.next
        if left:
            temp.next = left
        else:
            temp.next = right
        return dummy.next

    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        middle = self.getMid(head)
        left = head
        right = middle.next
        middle.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)