class Solution:
    def solution_166_2_1(self, tickets: List[List[str]]) -> List[str]:
        digraph = defaultdict(list) #directed graph 
        for fm, to in tickets: heappush(digraph[fm], to)
        
        def solution_166_2_2(n):
            """Hierholzer's algo to traverse every edge exactly once"""
            while digraph[n]: solution_166_2_2(heappop(digraph[n]))
            ans.appendleft(n)
        
        ans = deque() 
        solution_166_2_2("JFK")
        return ans