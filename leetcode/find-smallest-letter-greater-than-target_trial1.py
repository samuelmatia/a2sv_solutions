class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l,r = 0, n

        while l<r :
            m = (l+r)//2
            if letters[m] <= target : 
                l = m+1
            
            else : 
                r = m

        return letters[l%n]
        