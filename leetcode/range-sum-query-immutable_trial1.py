class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        nums2 = self.nums[left:right+1]
        n = len(nums2)
        prefix = [0] * n
        prefix[0] = nums2[0]

        for i in range(1,n) : 
            prefix[i] = prefix[i-1] + nums2[i]

        return prefix[-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)