class Solution:
    def solution_882_4(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        distances = [[float("inf")]*n for _ in range(n)]
        for city1,city2,dist in edges:
            distances[city1][city2] = dist
            distances[city2][city1] = dist

        for city in range(n):
            distances[city][city] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][via]+distances[via][j])            
        
        best_count = n+1
        city = -1
        for src_city in range(n):
            count = 0
            for dist in distances[src_city]:
                if dist <= distanceThreshold:
                    count += 1

            if count <= best_count:
                best_count = count
                city = src_city

        return city