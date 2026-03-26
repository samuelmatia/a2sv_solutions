class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
      
        n = len(nums)
        if k > n:
            return 0
        
        freq = defaultdict(int) 
        curr_sum = 0
        max_sum = 0
        left = 0

        for right in range(n):
           
            curr_sum += nums[right]
            freq[nums[right]] += 1

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                curr_sum -= nums[left]
                left += 1

          
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum
        