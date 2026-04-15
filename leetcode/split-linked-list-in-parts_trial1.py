# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head

        while curr : 
            curr = curr.next
            n += 1

        main_len, supp_len = n//k, n%k

        curr = head
        output= []

        for i in range(k) : 
            output.append(curr)

            for j in range(main_len-1+ (1 if supp_len else 0)) : 
                if not curr : break
                curr = curr.next

            supp_len -=  (1 if supp_len else 0)

            if curr : 
                curr.next, curr = None, curr.next

        
        return output
        

            

        

        