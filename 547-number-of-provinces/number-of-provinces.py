class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0] * n

        def dfs(city):
            vis[city] = 1
            for neigb, connected in enumerate(isConnected[city]):
                if vis[neigb] == 0 and connected == 1:
                    dfs(neigb)

        prov = 0
        for city in range(n):
            if vis[city] == 0:
                dfs(city)
                prov += 1

        return prov