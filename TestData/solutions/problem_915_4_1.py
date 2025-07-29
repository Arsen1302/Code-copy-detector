class Solution:
    def solution_915_4_1(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinate = dict() #employee tree
        for i, m in enumerate(manager): subordinate.setdefault(m, []).append(i) 
        
        def solution_915_4_2(node): 
            return informTime[node] + max((solution_915_4_2(n) for n in subordinate.get(node, [])), default=0)
        
        return solution_915_4_2(headID)