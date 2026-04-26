class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def test_k(k) : 
            h_test = 0

            for x in piles : 
                h_test += ceil(x/k)

            return h_test <= h

        left = 1
        right = max(piles)

        while left < right : 
            mid = (left+right)//2
            if test_k(mid) : 
                right = mid

            else : 
                left = mid+1       

        return right  