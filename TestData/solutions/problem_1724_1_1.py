class Solution:
    def solution_1724_1_1(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        def solution_1724_1_2(u, p):
            cnt = 1
            for v in graph[u]:
                if v == p: continue
                cnt += solution_1724_1_2(v, u)
            if u != 0:
                self.ans += math.ceil(cnt / seats)  # number of litters for `cnt` people to travel from node `u` to node `p`
            return cnt
                
        self.ans = 0
        solution_1724_1_2(0, -1)
        return self.ans