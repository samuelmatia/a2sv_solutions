class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        negatif = num < 0
        nombre = str(abs(num))
        
        liste = []
        zeros = 0

        for i in nombre:
            if i == '0':
                zeros += 1
            else:
                liste.append(int(i))
        
        if not negatif:
            liste.sort()
            
            premier = liste[0]

            resultat = str(premier)
            resultat += '0' * zeros
            resultat += ''.join(map(str, liste[1:]))
            
            return int(resultat)
        
        else:
            liste.sort(reverse=True)
            resultat = ''.join(map(str, liste))
            resultat += '0' * zeros
            
            return -int(resultat)