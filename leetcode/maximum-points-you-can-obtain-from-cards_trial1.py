class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        left = 0
        window = sum(cardPoints[:n-k])
        local = window

        for right in range(n-k, n) :
            local += cardPoints[right] - cardPoints[left] 
            window = min(window, local)
            left += 1

        return total-window  
