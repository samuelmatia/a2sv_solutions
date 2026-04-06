# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        n = 1
        while curr.next : 
            curr = curr.next
            n += 1
        
        curr.next = head
        m = k%n 
        l = n-m
        for _ in range(l) : 
            curr = curr.next
        curr = curr.next
        new_head = curr

        end =  new_head
        while end.next != new_head :
            end = end.next

        end.next = None

        return new_head      




        