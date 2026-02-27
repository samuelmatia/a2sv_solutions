class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        taille = len(points)
        
        for a in range(taille):
            dico = {}
            
            for b in range(taille):
                if a != b:
                    x1 = points[a][0]
                    y1 = points[a][1]
                    x2 = points[b][0]
                    y2 = points[b][1]
                    
                    distance = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                    
                    if distance in dico:
                        dico[distance] += 1
                    else:
                        dico[distance] = 1
            
            for nombre in dico.values():
                total += nombre * (nombre - 1)
        
        return total




            
        