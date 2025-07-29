class Solution:
    def solution_915_1_1(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def solution_915_1_2(i):
            if manager[i] != -1:
                informTime[i] += solution_915_1_2(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(solution_915_1_2, range(n)))