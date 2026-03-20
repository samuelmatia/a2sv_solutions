class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        somme = skill[0] + skill[-1]
        i = 0
        j = len(skill) - 1
        output = 0

        while i<j : 
            if (skill[i] + skill[j]) != somme : 
                return -1
            
            output += skill[i]*skill[j]

            i+= 1
            j-= 1

        return output




        