class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n

        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats
        

        output = [0] * n
        output[0] = diff[0]
        
        for i in range(1, n):

            
            output[i] = output[i - 1] + diff[i]
        
        return output
        