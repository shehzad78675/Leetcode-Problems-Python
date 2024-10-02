class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        m = len(flights)
        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for i in range(m):
            u = flights[i][0]
            v = flights[i][1]
            wt = flights[i][2]

            adj_list[u].append([v, wt])


        dist = [float("inf")] * n
        q = deque()

        q.append((0, src, 0))
        dist[src] = 0

        while q:
            stop, node, cost = q.popleft()

            if stop > k:
                continue

            for flight in adj_list[node]:
                cos = cost + flight[1]
                if cos < dist[flight[0]] and stop <= k:
                    dist[flight[0]] = cos
                    q.append((stop+1, flight[0], cos))
        
        if dist[dst] == float("inf"):
            return -1
        
        return dist[dst]

        