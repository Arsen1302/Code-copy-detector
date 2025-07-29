class Solution:
    def solution_721_2(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {} # graph as adjacency list 
        for u, v in paths: 
            graph.setdefault(u-1, []).append(v-1)
            graph.setdefault(v-1, []).append(u-1)
            
        ans = [0]*n
        for i in range(n): 
            ans[i] = ({1,2,3,4} - {ans[ii] for ii in graph.get(i, [])}).pop()
        return ans