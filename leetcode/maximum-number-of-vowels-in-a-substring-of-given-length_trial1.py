class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        number_vow = 0
        for i in s[:k] :
            if i in vowels : 
                number_vow += 1
        
        left = 0
        current = number_vow

        for right in range(k, len(s)) :
            if s[right] in vowels : 
                current += 1
            
            if s[left] in vowels : 
                current -= 1

            left+=1

            number_vow = max(current, number_vow)

        return number_vow



        