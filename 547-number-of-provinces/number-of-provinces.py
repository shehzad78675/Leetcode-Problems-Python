class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0] * n

        def dfs(city):
            vis[city] = 1
            q = deque()
            q.append(city)
            while q:
                node = q.popleft()

                for neigb, connected in enumerate(isConnected[node]):
                    if vis[neigb] == 0 and connected == 1:
                        vis[neigb] = 1
                        q.append(neigb)

        prov = 0
        for city in range(n):
            if vis[city] == 0:
                dfs(city)
                prov += 1

        return prov