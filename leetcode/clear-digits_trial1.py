class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        output = []

        for char in s :
            if char.isdigit() and output :
                output.pop()
            
            else: 
                output.append(char)


        return "".join(output) 

        
        