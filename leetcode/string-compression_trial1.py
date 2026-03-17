class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i, j = 0, 0
        write = 0

        while j < n:
            i = j

            while j < n and chars[j] == chars[i]:
                j += 1

            count = j - i

            chars[write] = chars[i]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write