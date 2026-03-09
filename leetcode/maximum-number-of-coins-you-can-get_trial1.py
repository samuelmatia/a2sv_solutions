class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)

        piles2 = [0]*n
        m = n//3
        sub = piles[-m:]

        i = 0
        j = 0
        for idx in range(n) : 
            if (idx+1)%3==0 :
                piles2[idx] = sub[j]
                j+=1
                
            elif (idx+1)%3 !=0 : 
                piles2[idx] = piles[i]
                i+=1 

        print(piles2)
        l = 0

        for idx, num in enumerate(piles2) : 
            if (idx+1)%3==2 : 
                l += piles2[idx]

        return l 
        