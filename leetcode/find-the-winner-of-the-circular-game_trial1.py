class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        array = list(range(1, n+1))
        index = 0
        while len(array) > 1 : 
            index = (index+k-1) % len(array)
            array.pop(index)

        return array[0]

             

        