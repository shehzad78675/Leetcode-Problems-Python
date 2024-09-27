class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        time = 0
        dric = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            row, col, t = q.popleft()
            time = max(time, t)
            for i in range(4):
                nrow = row + dric[i][0]
                ncol = col + dric[i][1]

                if nrow >= 0 and nrow < m and  ncol >= 0 and ncol < n and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    q.append((nrow, ncol, t + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return time

        
