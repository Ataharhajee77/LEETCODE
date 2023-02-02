## Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        
        for _ in range(n):
            if p2:
                p2 = p2.next
            else:
                break
        
        if p2==None:
            return head.next
        
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next
        return head
