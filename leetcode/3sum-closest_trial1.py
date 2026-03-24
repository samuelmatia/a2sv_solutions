class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        output = 0
        fixed = 0
        closest = float('inf')

        while fixed < len(nums) - 2 : 
            i = fixed+1
            j = len(nums)-1

            if fixed > 0 and nums[fixed] == nums[fixed-1] : 
                fixed += 1
                continue

            while i<j : 
                somme = nums[fixed] + nums[i] + nums[j]
                
                if abs(somme-target) < closest : 
                    output = somme
                    closest = abs(somme-target)

                if somme == target : 
                    return somme

                elif somme > target : 
                    j -= 1

                elif somme < target : 
                    i += 1

            fixed += 1

        return output 


        
