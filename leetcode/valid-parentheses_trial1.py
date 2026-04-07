class Solution:
    def isValid(self, s: str) -> bool:
        dico = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for char in s : 
            if char in dico.values() : 
                stack.append(char)
            
            else : 
                if not stack : 
                    return False

                popped = stack.pop()
                if dico[char] != popped : 
                    return False

        return len(stack) == 0


        
