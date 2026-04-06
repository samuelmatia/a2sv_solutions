# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(None, head)
        slow = dummy
        fast = dummy

        while fast.next : 
            fast = fast.next.next
            slow = slow.next

        slow = slow.next
        prev = None
        while slow :
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        maximum = float('-inf')
        left = head
        right = prev

        while right : 
            somme = left.val + right.val
            maximum = max(maximum, somme)

            left = left.next
            right = right.next

        return maximum

        