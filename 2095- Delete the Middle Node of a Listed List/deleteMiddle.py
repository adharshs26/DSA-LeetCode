# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n=0
        cur=head
        while cur:
            cur=cur.next
            n+=1
        n=n//2
        cur=head
        while n!=0:
            prev=cur
            cur=cur.next
            n-=1
        prev.next=cur.next
        return head
        