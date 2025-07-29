class Solution:
    def solution_915_5(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinate = dict() #employee tree
        for i, m in enumerate(manager): subordinate.setdefault(m, []).append(i) 
        
        ans = 0
        stack = [(headID, 0)] #id-time
        while stack: #dfs 
            i, t = stack.pop()
            ans = max(ans, t)
            for ii in subordinate.get(i, []): stack.append((ii, t + informTime[i]))
        return ans