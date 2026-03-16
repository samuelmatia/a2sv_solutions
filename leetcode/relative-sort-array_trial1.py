class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        dico = {}
        for num in arr1 : 
            dico[num] = dico.get(num, 0)+1
        
        output = [0] * len(arr1)
        idx = 0

        for num in arr2:
            for _ in range(dico[num]):
                output[idx] = num
                idx += 1
            del dico[num]
        
        remaining = []
        for num, count in dico.items():
            remaining.extend([num] * count)
        remaining.sort()


        for num in remaining:
            output[idx] = num
            idx += 1

        return output
        