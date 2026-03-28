class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        output = 0
        n = len(nums)

        left = 0
        freq = set()
        somme = 0
 
        for right in range(n) :
            while nums[right] in freq :
                freq.remove(nums[left])
                somme -= nums[left]
                left += 1

            freq.add(nums[right])
            somme += nums[right]
            output = max(output, somme)

        return output
