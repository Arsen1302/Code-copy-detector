class Solution:
    def solution_1208_3(self, cars: List[List[int]]) -> List[float]:
        ans = [-1]*len(cars)
        stack = []
        for i, (x, v) in enumerate(reversed(cars)): 
            while stack and (v <= stack[-1][1] or (stack[-1][0] - x)/(v - stack[-1][1]) >= stack[-1][2]): stack.pop()
            if stack: 
                t = (stack[-1][0] - x)/(v - stack[-1][1])
                stack.append((x, v, t))
                ans[~i] = t
            else: 
                stack.append((x, v, inf))
        return ans