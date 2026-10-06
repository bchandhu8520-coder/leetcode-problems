class Solution:
    def uniquePathsIII(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        empty = 0
        start_row = 0
        start_col = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    empty += 1

                if grid[r][c] == 1:
                    start_row = r
                    start_col = c

        def backtrack(r, c, count):
            if grid[r][c] == 2:
                if count == empty:
                    return 1
                return 0

            temp = grid[r][c]
            grid[r][c] = -1

            paths = 0

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != -1:
                        paths += backtrack(nr, nc, count + 1)

            grid[r][c] = temp

            return paths

        return backtrack(start_row, start_col, 1)