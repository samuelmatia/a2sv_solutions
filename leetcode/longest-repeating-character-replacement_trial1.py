class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1 : 
            return 1
            
        left = 0
    
        window = {}
        window[s[left]] = 1
        output = 0

        size = 1

        for right in range(1, len(s)) :
            window[s[right]] = window.get(s[right], 0)+1
            size += 1

            max_freq = max(list(window.values()))
            remplacements = size - max_freq


            while remplacements > k :
                size -= 1

                window[s[left]] -=  1 
                
                max_freq = max(list(window.values()))
                remplacements = size - max_freq
                left += 1

            output = max(output, size)

        return output

                


           


            





