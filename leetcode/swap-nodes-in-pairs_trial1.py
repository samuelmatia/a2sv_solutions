# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
    
        prev = dummy
        curr = head

        while curr and curr.next : 
            
            nextnextNode = curr.next.next
            nextNode = curr.next

            nextNode.next = curr
            curr.next = nextnextNode
            prev.next = nextNode

            prev = curr
            curr = nextnextNode


        return dummy.next

        