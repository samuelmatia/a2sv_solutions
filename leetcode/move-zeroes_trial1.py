class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l1 = 0
        l2 = 1
        while l2 <= len(nums)-1 : 
            if nums[l1] == 0 and nums[l2] != 0 : 
                nums[l1], nums[l2] = nums[l2], nums[l1]
                l1 += 1
                l2 += 1

            elif nums[l1] != 0 and nums[l2] != 0 : 
                l1 += 1
                l2 += 1

            elif nums[l1] != 0 and nums[l2] == 0 : 
                l1 += 1
                l2 += 1

            else : 
                l2 += 1
