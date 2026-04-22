class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daystaken(capacity) : 
            day = 1
            count = 0

            for w in weights : 
                count+= w
                if count > capacity : 
                    day += 1
                    count = w

            return day



        low = max(weights)
        high = sum(weights)

        while low<=high : 
            mid = (low+high)//2

            if daystaken(mid) <= days :
                high = mid-1

            else : 
                low = mid+1
            
        return low


        