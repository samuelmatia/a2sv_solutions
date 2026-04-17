# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr1 = list1
        ptr2 = list2
        current = dummy

        while ptr1 and ptr2 :
            if ptr1.val<=ptr2.val : 
                current.next = ptr1
                ptr1 = ptr1.next
            else : 
                current.next = ptr2
                ptr2 = ptr2.next

            current = current.next

        while ptr1 : 
            current.next = ptr1
            ptr1 = ptr1.next 
            current = current.next

        while ptr2 : 
            current.next = ptr2
            ptr2 = ptr2.next
            current = current.next  
            
        return dummy.next
        
        