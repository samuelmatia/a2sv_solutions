class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        dico = {}

        for idx, scor in enumerate(sorted_score) :
            dico[scor] = idx

        ans = []

        for sc in score : 
            if dico[sc] == 0 :
                ans.append("Gold Medal")

            elif dico[sc] == 1 : 
                ans.append("Silver Medal")

            elif dico[sc] == 2 : 
                ans.append("Bronze Medal")

            else : ans.append(str(dico[sc]+1))

        return ans 
         



        