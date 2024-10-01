class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        q = deque()
        dist = [[0] * n for i in range(m)]
        vis = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    vis[i][j] = 1

       
        dric = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            row, col, dis = q.popleft()
            dist[row][col] = dis

            for i in range(4):
                nrow = row + dric[i][0]
                ncol = col + dric[i][1]

                if nrow >= 0 and nrow < m and  ncol >= 0 and ncol < n and vis[nrow][ncol] == 0:
                
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol, dis + 1))
        
        return dist