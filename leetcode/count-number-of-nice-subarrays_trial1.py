class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        frequences = {0: 1}

        for num in nums:
            if num % 2 == 1:
                prefix += 1

            if prefix - k in frequences:
                count += frequences[prefix - k]

            frequences[prefix] = frequences.get(prefix, 0) + 1

        return count
        


                 

        