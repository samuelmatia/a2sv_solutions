class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        liste = []

        for idx, num in enumerate(sorted(nums)) : 
            if num == target : 
                liste.append(idx)

        return liste
        