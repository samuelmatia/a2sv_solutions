# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        ptr1 = l1
        ptr2 = l2
        carry = 0
        result = dummy

        while ptr1 or ptr2 or carry:
            v1 = ptr1.val if ptr1 else 0
            v2 = ptr2.val if ptr2 else 0

            somme = v1 + v2 + carry

            carry = somme // 10
            rep = somme % 10


            result.next = ListNode(rep)
            result = result.next


            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        return dummy.next