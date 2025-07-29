class Solution:
    def solution_444_5(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [sys.maxsize] * n
        dp[k-1] = 0
        graph = collections.defaultdict(list)
        for s, e, w in times:
            graph[s].append((e, w))
            
        dq = collections.deque([k])
        visited = set([k])
        while dq:
            node = dq.popleft()
            cost = dp[node-1]
            visited.remove(node)
            for nei, w in graph[node]:
                if dp[nei-1] > cost + w:
                    dp[nei-1] = cost + w
                    if nei not in visited:
                        visited.add(nei)
                        dq.append(nei)
        
        ans = 0                    
        for i in range(n):
            if i != k-1:
                ans = max(ans, dp[i])
        return ans if ans != sys.maxsize else -1