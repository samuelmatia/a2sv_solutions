class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5 : 
            return 0

        output = 0 
        vowels = ["a", "e", "i", "o", "u"]

        left = 0
        while left < len(word) - 4 : 
            for right in range(left+4, len(word)) : 
                sub = word[left:right+1]
                sub = list(set(list(sub)))
                sub.sort()
                if sub == vowels :
                    output += 1

            left += 1
        return output


             
        