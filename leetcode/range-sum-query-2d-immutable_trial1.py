class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * n for _ in range(m)]


        self.prefix[0][0] = matrix[0][0]


        for j in range(1, n):
            self.prefix[0][j] = self.prefix[0][j-1] + matrix[0][j]


        for i in range(1, m):
            self.prefix[i][0] = self.prefix[i-1][0] + matrix[i][0]

        for i in range(1, m):
            for j in range(1, n):
                self.prefix[i][j] = (
                    self.prefix[i-1][j]
                    + self.prefix[i][j-1]
                    - self.prefix[i-1][j-1]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        double = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        subst1 = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        subst2 = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        return total - subst1 - subst2 + double