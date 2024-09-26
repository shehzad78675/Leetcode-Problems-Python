class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        prov = 0


        vis = [0] * cities
        def dfs(city):
            vis[city] = 1

            for neigb, connected in enumerate(isConnected[city]):
                if vis[neigb] == 0 and connected == 1:
                    dfs(neigb)


        for city in range(cities):
            if vis[city] == 0:
                dfs(city)
                prov += 1

            
        return prov