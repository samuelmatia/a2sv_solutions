class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        output = 0

        i = 0
        j = len(nums)-1

        while i < j : 
            if nums[i] + nums[j] < target : 
                output += (j-i)
                i += 1

            else : 
                j-=1

        return output
        