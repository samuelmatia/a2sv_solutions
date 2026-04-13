class Solution:
    def firstUniqChar(self, s: str) -> int:
        dico = {}
        for c in s :
            dico[c] = dico.get(c, 0) + 1
        
        print(dico)

        for k,v in dico.items() : 
            if v == 1 :
                return s.index(k)

        return -1

        