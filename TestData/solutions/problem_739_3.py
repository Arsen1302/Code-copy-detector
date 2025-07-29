class Solution:
    def solution_739_3(self, s: str) -> str:
        d=Counter(s)
        vis=[False]*26
        stack=[]
        n=len(s)
        for i in range(n):
            while stack and s[i]<stack[-1] and d[stack[-1]]>0 and not vis[ord(s[i])-97]:
                vis[ord(stack[-1])-97]=False
                stack.pop()
            
            d[s[i]]-=1
            if not vis[ord(s[i])-97]:
                vis[ord(s[i])-97]=True
                stack.append(s[i])
        print(stack)
        return "".join(stack)