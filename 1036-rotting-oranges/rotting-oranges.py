class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        vis = []

        not_rotten = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    not_rotten += 1
        
        drow = [1,0,-1,0]
        dcol = [0,-1,0,1]

        cnt = 0
        tm = 0
        while q:
            row, col, time = q.popleft()
            tm = max(tm, time)
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]

                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    cnt += 1
                    q.append((nrow, ncol, time+1))

        if cnt != not_rotten:
            return -1

        return tm
