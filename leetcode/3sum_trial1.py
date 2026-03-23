class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3 : 
            return []

        output = []

        nums.sort()
        fixed = 0

        while fixed < len(nums)-2 :
            if fixed > 0 and nums[fixed-1] == nums[fixed] : 
                fixed += 1
                continue

            i = fixed+1
            j = len(nums) -1


            while i < j :
                a = nums[i] + nums[j]
                if a + nums[fixed] == 0 : 
                    output.append([nums[fixed], nums[i], nums[j]])
                    
                    while i<j and nums[i] == nums[i+1] : 
                        i+= 1
                    
                    while i<j and nums[j] == nums[j-1] : 
                        j-= 1

                    i+= 1
                    j-= 1

                    
                
                elif a + nums[fixed] < 0 : 
                    i += 1

                elif a + nums[fixed] > 0 :
                    j -= 1

            fixed += 1

        return output
             

                    



        
        