class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for start in range(n):
            count_adjacent = 0
            for end in range(start, n):
                if end > start and s[end] == s[end - 1]:
                    count_adjacent += 1
                if count_adjacent > 1:
                    break  
                max_len = max(max_len, end - start + 1)

        return max_len
        