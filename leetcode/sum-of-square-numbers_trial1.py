class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5) 
        

        while a <= b:
            result = a*a + b*b
            
            if result == c:
                return True
            elif result < c:
                a += 1
            else:
                b -= 1
        
        return False
        