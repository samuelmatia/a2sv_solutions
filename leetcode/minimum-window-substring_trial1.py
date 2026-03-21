class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size = len(s)
        left = 0

        char_counter = Counter(t)
        total_char = 0 

        min_str = ""
        min_len = float('inf')


        for right in range(size):
            curr = s[right]


            if curr in char_counter:
                char_counter[curr] -= 1
                if char_counter[curr] == 0:
                    total_char += 1


            while total_char == len(char_counter):

                left_char = s[left]
                if left_char in char_counter:
                    if char_counter[left_char] == 0:
                        total_char -= 1
                    char_counter[left_char] += 1
                

                if (right - left + 1) < min_len :
                    min_len = (right - left + 1)      
                    min_str = s[left:right + 1]

                left += 1
        return min_str