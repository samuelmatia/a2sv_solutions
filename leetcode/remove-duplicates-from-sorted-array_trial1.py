class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums : 
            return 0

        slow = 0
        fast = 1

        while fast <= len(nums)-1 : 
            if nums[slow] != nums[fast] :
                slow += 1
                nums[slow] = nums[fast]
            fast+=1

        return slow+1 


        
                  

        