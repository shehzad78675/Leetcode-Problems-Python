class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        dist = [[0] * m for i in range(n)]
        vis = [[0] * m for i in range(n)]

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    vis[i][j] = 1
                    q.append((i, j, 0))

        drow = [1,0,-1,0]
        dcol = [0,-1,0,1]

        while q:
            row, col, dis = q.popleft()

            dist[row][col] = dis
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vis[nrow][ncol] == 0:
                        q.append((nrow, ncol, dis + 1))
                        vis[nrow][ncol] = 1
        
        return dist
