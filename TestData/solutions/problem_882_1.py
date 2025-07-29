class Solution:
    def solution_882_1(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """Floyd-Warshall algorithm"""
        dist = [[float("inf")]*n for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for i, j, w in edges: dist[i][j] = dist[j][i] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = {sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
        return ans[min(ans)]