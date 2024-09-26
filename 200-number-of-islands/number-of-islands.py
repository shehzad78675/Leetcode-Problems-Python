class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        n = len(grid)
        m = len(grid[0])

        def dfs(row, col, vis):
            vis[row][col] = 1
            drow = [0,-1,0,1]
            dcol = [1,0,-1,0]

            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == "1":
                    dfs(nrow, ncol, vis)

        vis = [[0] * m for i in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j, vis)

        return cnt


