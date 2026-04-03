# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head : 
            return head
        list1 = ListNode(None)
        list2 = ListNode(None)

        p1 = list1
        p2 = list2

        curr = head
        while curr :
            temp = curr.next 
            if curr.val < x :
                p1.next = curr
                curr.next = None
                p1 = p1.next
            else : 
                p2.next = curr
                curr.next = None
                p2 = p2.next
            curr = temp

        p1.next = list2.next 
        

        return list1.next if list1.next else list2.next

        