class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        if not firstList or not secondList : 
            return []

        output = []
        
        i = j = 0

        while i<len(firstList) and j<len(secondList) : 
            a,b = firstList[i]
            c,d = secondList[j]

            if max(a,c) <= min(b,d) : 
                output.append([max(a,c), min(b,d)])

            if b<d : 
                i+= 1
            else : 
                j+=1

        return output



        
        