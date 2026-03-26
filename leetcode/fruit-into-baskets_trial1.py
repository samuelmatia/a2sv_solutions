class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dico = {} 
        left = 0
        output = 0  
        
        for right, fruit in enumerate(fruits):

            dico[fruit] = dico.get(fruit, 0) + 1
            

            while len(dico) > 2:
                left_fruit = fruits[left]
                dico[left_fruit] -= 1
                if dico[left_fruit] == 0:
                    del dico[left_fruit]
                left += 1
            
            output = max(output, right - left + 1)
        
        return output

        