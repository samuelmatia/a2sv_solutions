class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        count = sum(1 for c in blocks[:k] if c == 'W')
        min_oper = count

        for i in range(1, n - k + 1):
 
            if blocks[i - 1] == 'W':
                count -= 1

            if blocks[i + k - 1] == 'W':
                count += 1

            min_oper = min(min_oper, count)

        return min_oper
        