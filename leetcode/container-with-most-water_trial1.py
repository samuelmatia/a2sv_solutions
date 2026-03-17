class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1

        output = float('-inf')
        
        while i<j : 
            width = j-i
            heigh = min(height[i], height[j])
            area = width*heigh
            
            output = max(output, area)

            if height[i] <= height[j] : 
                i+=1
            else : 
                j-=1

        return output

            



        