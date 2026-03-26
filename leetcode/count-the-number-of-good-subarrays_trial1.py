class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        pairs = 0
        result = 0
        n = len(nums)

        for right in range(n):
            x = nums[right]

            count_x = freq.get(x, 0)
            pairs += count_x
            freq[x] = count_x + 1

           
            while pairs >= k:
                result += (n - right)
                
                y = nums[left]
                freq[y] -= 1
                pairs -= freq[y]  
                left += 1

        return result