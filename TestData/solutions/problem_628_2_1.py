class Solution:
    def solution_628_2_1(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [False]*n
        rows = defaultdict(list)
        cols = defaultdict(list)
        ans = 0
        for i,point in enumerate(stones):
            rows[point[0]].append(i)
            cols[point[1]].append(i)
        
        def solution_628_2_2(node):
            visited[node] = True
            count = 1
            for x in rows[stones[node][0]]:
                if visited[x] == False:
                    count += solution_628_2_2(x)
            for x in cols[stones[node][1]]:
                if visited[x] == False:
                    count += solution_628_2_2(x)
            return count
            
        for i in range(n):
            if visited[i] == False:
                size = solution_628_2_2(i)
                ans += size-1
        return ans