# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy
        curr = head

        for _ in range(left-1) :
            prev = curr
            curr = curr.next

        move = None

        for _ in range(right-left+1) : 
            temp = curr.next
            curr.next = move
            move = curr
            curr = temp

        prev.next.next = curr
        prev.next = move

        return dummy.next







        