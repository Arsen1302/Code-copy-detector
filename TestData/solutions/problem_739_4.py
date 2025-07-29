class Solution:
    def solution_739_4(self, s: str) -> str:
        d={v:k for k,v in enumerate(s)}
        stack=[]
        for k,v in enumerate(s):
            if v not in stack:
                while stack and stack[-1]>v and d[stack[-1]]>k:
                    stack.pop()
                stack.append(v)
        return "".join(stack)