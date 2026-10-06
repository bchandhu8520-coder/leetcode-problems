class Solution:
    def totalNQueens(self, n):
        columns = set()
        diagonal1 = set()
        diagonal2 = set()

        def backtrack(row):
            if row == n:
                return 1

            total = 0

            for col in range(n):
                if col in columns:
                    continue

                if row - col in diagonal1:
                    continue

                if row + col in diagonal2:
                    continue

                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                total += backtrack(row + 1)

                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

            return total

        return backtrack(0)