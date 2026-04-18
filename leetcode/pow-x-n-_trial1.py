class Solution:
    def myPow(self, x: float, n: int) -> float:
        def exp(x,n) : 
            if x== 0 : 
                return 0
            if n == 0 : 
                return 1
            
            output = exp(x, n//2)
            output = output*output
            
            return x*output if n%2==1 else output
        
        sortie = exp(x, abs(n))
        
        return sortie if n >= 0 else 1/sortie
        