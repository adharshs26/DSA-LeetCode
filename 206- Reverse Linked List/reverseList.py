# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        front = None
        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev

        