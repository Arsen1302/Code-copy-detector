class Solution:
    def solution_444_2(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [sys.maxsize] * n
        dp[k-1] = 0
        graph = collections.defaultdict(list)
        for s, e, w in times:
            graph[s].append((e, w))
        visited = set()    
        heap = [(0, k)]            
        while heap:
            cur, node = heapq.heappop(heap)
            dp[node-1] = cur
            if node not in visited:
                visited.add(node)
                n -= 1
            for nei, w in graph[node]:
                if dp[nei-1] > cur + w:
                    dp[nei-1] = cur + w
                    if nei not in visited:
                        heapq.heappush(heap, (cur + w, nei))
            if not n: return cur
        return -1