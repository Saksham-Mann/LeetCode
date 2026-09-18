# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getk(self, curr: ListNode, k: int) -> ListNode | None:
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        test=ListNode(0)
        test.next=head
        dummy=test
        while True:
            kt=self.getk(dummy,k)
            if not kt:
                break
            nextNode=kt.next
            prev=nextNode
            curr=dummy.next
            for _ in range(k):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=dummy.next
            dummy.next=kt
            dummy=temp
        return test.next
