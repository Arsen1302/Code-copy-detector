class Solution:
    def solution_475_5_1(self, graph: List[List[int]]) -> bool:
        numNode = len(graph)
        set1 = [False for _ in range(numNode)]
        set2 = [False for _ in range(numNode)]
        
        for i in range(numNode):
            if (set1[i] or set2[i]): 
                continue
            if (not self.solution_475_5_2(i, set1, set2, graph)):
                return False
        
        return True
    
    def solution_475_5_2(self, cur: int, set1: List[bool], set2: List[bool], graph: List[List[int]]) -> bool:
        if (set1[cur]):
            return not set2[cur]
        
        set1[cur] = True
        
        for n in graph[cur]:
            if (not self.solution_475_5_2(n, set2, set1, graph)):
                return False
        
        return True