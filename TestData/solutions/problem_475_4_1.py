class Solution:
    def solution_475_4_1(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        u = [i for i in range(n)]
        
        def solution_475_4_2(i):
            if i == u[i]: return i
            else: 
                u[i] = solution_475_4_2(u[i])
                return u[i]
            
        def solution_475_4_3(a, b):
            r_a = solution_475_4_2(a)
            r_b = solution_475_4_2(b)
            if r_a != r_b: 
                u[r_a] = r_b
                u[a] = r_b
                
        for g in range(len(graph)):
            root = solution_475_4_2(g)
            for i in range(1, len(graph[g])):
                solution_475_4_3(graph[g][i], graph[g][i-1])
                if root == solution_475_4_2(graph[g][i]) or root == solution_475_4_2(graph[g][i - 1]):
                    return False
        return True