class Solution:
    def solution_915_2_1(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:        
        def solution_915_2_2(n: int) -> int:
            if manager[n] != -1:
                informTime[n] += solution_915_2_2(manager[n])
                manager[n] = -1
            return informTime[n]
        
        for idx in range(len(manager)):
            solution_915_2_2(idx)
            
        return max(informTime)