class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        right = len(arr) - 1
        output = []

        while right > 0:

            max_idx = 0
            for i in range(right + 1):
                if arr[i] > arr[max_idx]:
                    max_idx = i

    
            if max_idx == right:
                right -= 1
                continue

 
            if max_idx != 0:
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                output.append(max_idx + 1)

            arr[:right + 1] = arr[:right + 1][::-1]
            output.append(right + 1)

            right -= 1

        return output

            



        
        