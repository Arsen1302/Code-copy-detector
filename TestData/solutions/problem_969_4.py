class Solution:
    def solution_969_4(self, n: int) -> List[str]:
        ans = []
        stack = [(0, 1, 1, 1)]
        while stack: 
            px, pd, x, d = stack.pop()
            cx = px + x # mediant
            cd = pd + d
            if cd <= n: 
                stack.append((cx, cd, x, d))
                stack.append((px, pd, cx, cd))
                ans.append(f"{cx}/{cd}")
        return ans