class Solution:
    def solution_991_5(self, p: List[int]) -> List[int]:
        
        n=len(p)
        stack =[]
        ans=[]
        
        for j in range(n-1,-1,-1):
            
            while stack and stack[-1]>p[j]:
                stack.pop()
            
            if len(stack)==0:
                ans.append(p[j])
            else:
                ans.append(p[j]-stack[-1])
            stack.append(p[j])
        return ans[::-1]