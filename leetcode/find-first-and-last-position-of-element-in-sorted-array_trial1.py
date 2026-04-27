class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def starting() :
            left, right = 0, len(nums)-1
            output = -1

            while left<=right : 
                m = (left+right)//2
                if nums[m] >= target :
                    right = m-1
                
                elif nums[m] < target : 
                    left = m+1
                
                if nums[m] == target : 
                    output = m
            return output

        def ending() :
            left, right = 0, len(nums)-1
            output = -1

            while left<=right : 
                m = (left+right)//2
                if nums[m] > target :
                    right = m-1
                
                elif nums[m] <= target : 
                    left = m+1
                
                if nums[m] == target : 
                    output = m
            return output


        return [starting(), ending()]

