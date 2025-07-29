class Solution:
    def solution_762_3(self, arr: List[int]) -> int:
        ans = 0 
        stack = []
        for x in arr: 
            while stack and stack[-1] <= x: 
                val = stack.pop()
                ans += val * min(stack[-1] if stack else inf, x)
            stack.append(x)
        return ans + sum(stack[i-1]*stack[i] for i in range(1, len(stack)))