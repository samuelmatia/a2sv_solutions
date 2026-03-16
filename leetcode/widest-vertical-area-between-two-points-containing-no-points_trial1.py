class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        coord_x = sorted([x for x,_ in points])
        maximum = 0

        i = 0
        for j in range(1,len(coord_x)) : 
            maximum = max(maximum, coord_x[j] - coord_x[i])
            i+=1
        
        return maximum
        