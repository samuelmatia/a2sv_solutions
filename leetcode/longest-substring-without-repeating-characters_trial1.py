class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        string = list(s)
        sub = [string[0]]
        max_sub = sub.copy()
        
        left = 0
        right = 1

        while right < len(string):
            
            if string[right] not in sub:
                sub.append(string[right])

                if len(sub) > len(max_sub):
                    max_sub = sub.copy()

                right += 1

            else:
                sub.pop(0)
                left += 1

        return len(max_sub)