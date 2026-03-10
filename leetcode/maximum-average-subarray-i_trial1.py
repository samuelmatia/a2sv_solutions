class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum= sum(nums[:k])

        left = 0
        win_somme = max_sum

        for right in range(k, n) :
            win_somme += nums[right]
            win_somme -= nums[left]

            max_sum = max(win_somme, max_sum)

            left += 1 

        return max_sum/k
